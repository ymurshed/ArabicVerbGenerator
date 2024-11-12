using Serilog;
using ArabicVerbGenerator.Worker.Service.Extensions;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace ArabicVerbGenerator.Worker.Service
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureAppConfiguration((hostContext, configurationBuilder) =>
                {
                    var environmentName = hostContext.HostingEnvironment.EnvironmentName;
                    configurationBuilder.SetConfigurationRoot(environmentName);
                })
                .ConfigureServices((hostContext, services) =>
                {
                    hostContext.Configuration.ConfigLogger();
                    services.AddHostedService<Worker>();
                })
                .UseSerilog()
                .UseWindowsService();
    }
}
