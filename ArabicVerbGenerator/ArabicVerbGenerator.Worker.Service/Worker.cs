using NCrontab;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace ArabicVerbGenerator.Worker.Service
{
    public class Worker : BackgroundService
    {
        public static IConfigurationRoot Configuration { get; set; }

        private DateTime _nextRun;
        private bool _hasException;
        private readonly string _batchFilePath;
        private readonly string _cronScheduleConfig;
        private readonly CrontabSchedule _schedule;
        private readonly ILogger<Worker> _logger;
        private readonly IHostApplicationLifetime _applicationLifetime;

        public Worker(ILogger<Worker> logger, IHostApplicationLifetime applicationLifetime)
        {
            _hasException = false;
            _applicationLifetime = applicationLifetime;

            _logger = logger;
            _logger.LogInformation($"Inside Worker constructor at: {DateTime.Now}.");

            try
            {
                _batchFilePath = Configuration.GetValue<string>("BatchFilePath")!;
                _logger.LogInformation($"Batch file path: {_batchFilePath}");

                _cronScheduleConfig = Configuration.GetValue<string>("CronScheduleConfig")!;
                _logger.LogInformation($"Cron schedule configuration: {_cronScheduleConfig}");

                _schedule = CrontabSchedule.Parse(_cronScheduleConfig, new CrontabSchedule.ParseOptions { IncludingSeconds = false });
                _nextRun = _schedule.GetNextOccurrence(DateTime.Now);
                _logger.LogInformation($"First execution time after running the service: {_nextRun:G}");
            }
            catch (Exception ex)
            {
                _hasException = true;
                _logger.LogError($"Exception occurred inside Worker constructor at: {DateTime.Now}. Exception Details: {ex}");
            }
        }

        public override Task StartAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation($"ArabicVerbGenerator.Worker.Service started at: {DateTime.Now}");
            return base.StartAsync(cancellationToken);
        }

        public override Task StopAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation($"ArabicVerbGenerator.Worker.Service stopped at: {DateTime.Now}");
            return base.StopAsync(cancellationToken);
        }

        protected override async Task ExecuteAsync(CancellationToken cancellationToken)
        {
            await HandleException(cancellationToken);

            while (!cancellationToken.IsCancellationRequested)
            {
                var now = DateTime.Now;
                if (now > _nextRun)
                {
                    try
                    {
                        _logger.LogInformation($"ArabicVerbGenerator.Worker.Service is going to start executing batch file at: {now}");
                        System.Diagnostics.Process.Start(_batchFilePath);

                        _nextRun = _schedule.GetNextOccurrence(DateTime.Now);
                        _logger.LogInformation($"Next execution time: {_nextRun:G}");
                    }
                    catch (Exception ex)
                    {
                        _hasException = true;
                        _logger.LogError($"Exception occurred during batch file execution at: {DateTime.Now}. Exception Details: {ex}");
                    }

                    await HandleException(cancellationToken);
                }

                await Task.Delay(5000, cancellationToken);
            }
        }

        public async Task HandleException(CancellationToken cancellationToken)
        {
            if (!_hasException) return;
            _logger.LogCritical("Exiting ArabicVerbGenerator.Worker.Service due to exception.");
            _applicationLifetime.StopApplication();
            await Task.Delay(10000, cancellationToken);
        }
    }
}
