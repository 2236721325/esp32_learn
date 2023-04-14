using MauiCar.Services;
using MauiCar.ViewModels;
using MauiCar.Views;

namespace MauiCar
{
    public static class MauiProgram
    {
        public static MauiApp CreateMauiApp()
        {
            var builder = MauiApp.CreateBuilder();
            builder
                .UseMauiApp<App>()
                .ConfigureFonts(fonts =>
                {
                    fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
                    fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
                });


            builder.Services.AddSingleton<ScanPageViewModel>();
            builder.Services.AddSingleton<ScanPage>();

            builder.Services.AddSingleton<MainPage>();

            builder.Services.AddSingleton<ControlPage>();
            builder.Services.AddSingleton<ControlPageViewModel>();


            builder.Services.AddSingleton<BluetoothLEService>();

            return builder.Build();
        }
    }
}