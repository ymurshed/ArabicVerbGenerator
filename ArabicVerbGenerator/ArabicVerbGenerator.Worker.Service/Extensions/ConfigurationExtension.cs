using System.Reflection;
using Microsoft.Extensions.Configuration;
using Serilog;

namespace ArabicVerbGenerator.Worker.Service.Extensions
{
    public static class ConfigurationExtension
    {
        public static void SetConfigurationRoot(this IConfigurationBuilder configurationBuilder, string environmentName)
        {
            var appBasePath = Path.GetDirectoryName(Assembly.GetEntryAssembly()?.Location);
            var appSettingsFile = environmentName == "Development" ? $"appsettings.{environmentName}.json" : "appsettings.json";
            Console.WriteLine($"App base path to load appSettings: {appBasePath}");

            Worker.Configuration = configurationBuilder.SetBasePath(appBasePath!)
                .AddJsonFile(appSettingsFile, false, true)
                .AddEnvironmentVariables()
                .Build();
        }

        public static void ConfigLogger(this IConfiguration configuration)
        {
            Log.Logger = new LoggerConfiguration()
                .MinimumLevel.Information()
                .ReadFrom.Configuration(configuration)
                .CreateLogger();
        }
    }
}
