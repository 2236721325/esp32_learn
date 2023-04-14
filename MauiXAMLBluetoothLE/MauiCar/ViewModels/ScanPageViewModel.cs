using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using MauiCar.Models;
using MauiCar.Services;
using Plugin.BLE.Abstractions;
using Plugin.BLE.Abstractions.Exceptions;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MauiCar.ViewModels
{
    public partial class ScanPageViewModel:ObservableObject
    {
        public BluetoothLEService BLEService { get; set; }
        public ScanPageViewModel(BluetoothLEService ble )
        {
            BLEService = ble;
        }


        [ObservableProperty]
        List<DeviceCandidate> results;


        [RelayCommand]
        public async void Scan()
        {
            PermissionStatus status = await Permissions.CheckStatusAsync<Permissions.LocationWhenInUse>();
            if(status!=PermissionStatus.Granted)
            {
                await Permissions.RequestAsync<Permissions.LocationWhenInUse>();

            }

            Results = await BLEService.ScanForDevicesAsync();

        }



        


        public async Task ConnectToDeviceAsync(DeviceCandidate item)
        {
            try
            {
                var parameters = new ConnectParameters(forceBleTransport: true);
                await BLEService.Adapter.ConnectToDeviceAsync(item.Device,parameters);
                Debug.WriteLine("Connected Ok!");

                await Shell.Current.GoToAsync("//ControlPage");


            }
            catch (DeviceConnectionException e)
            {
                // ... could not connect to device
                Debug.WriteLine(e.Message);
                Debug.WriteLine(e.ToString());
            }
        }
    }
}
