using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using MauiCar.Services;
using Plugin.BLE.Abstractions.Contracts;

namespace MauiCar.ViewModels
{
    public partial class ControlPageViewModel:ObservableObject
    {
        public BluetoothLEService BLEService { get; set; }

        private  IService _IService;
        public ControlPageViewModel(BluetoothLEService ble)
        {
            BLEService = ble;

        }

        [RelayCommand]
        public async void Forward()
        {

            if (_IService == null)
            {
                _IService = await BLEService.Device.GetServiceAsync(Guid.Parse("6E400001-B5A3-F393-E0A9-E50E24DCCA9E"));
            }
            await WriteToCharacteristic(_IService, data: "forward", "6E400002-B5A3-F393-E0A9-E50E24DCCA9E");

        }


        [RelayCommand]
        public async void Down()
        {

            if (_IService == null)
            {
                _IService = await BLEService.Device.GetServiceAsync(Guid.Parse("6E400001-B5A3-F393-E0A9-E50E24DCCA9E"));
            }
            await WriteToCharacteristic(_IService, data: "down", "6E400002-B5A3-F393-E0A9-E50E24DCCA9E");

        }

        [RelayCommand]
        public async void Stop()
        {

            if (_IService == null)
            {
                _IService = await BLEService.Device.GetServiceAsync(Guid.Parse("6E400001-B5A3-F393-E0A9-E50E24DCCA9E"));
            }
            await WriteToCharacteristic(_IService, data: "stop", "6E400002-B5A3-F393-E0A9-E50E24DCCA9E");

        }

        [RelayCommand]
        public async void Left()
        {

            if (_IService == null)
            {
                _IService = await BLEService.Device.GetServiceAsync(Guid.Parse("6E400001-B5A3-F393-E0A9-E50E24DCCA9E"));
            }
            await WriteToCharacteristic(_IService, data: "left", "6E400002-B5A3-F393-E0A9-E50E24DCCA9E");

        }

        [RelayCommand]
        public async void Right()
        {

            if (_IService == null)
            {
                _IService = await BLEService.Device.GetServiceAsync(Guid.Parse("6E400001-B5A3-F393-E0A9-E50E24DCCA9E"));
            }
            await WriteToCharacteristic(_IService, data: "right", "6E400002-B5A3-F393-E0A9-E50E24DCCA9E");

        }


        private Task WriteToCharacteristic(IService service, string data, string guid)
        {
            return WriteToCharacteristic(service, System.Text.Encoding.UTF8.GetBytes(data), guid);
        }

        private async Task WriteToCharacteristic(IService service, byte[] data, string guid)
        {
            ICharacteristic characteristic = await service.GetCharacteristicAsync(Guid.Parse(guid));
            if (characteristic != null)
            {
                await characteristic.WriteAsync(data);
            }
        }
    }
}
