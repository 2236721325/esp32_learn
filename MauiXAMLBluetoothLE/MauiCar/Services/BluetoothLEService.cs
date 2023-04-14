using MauiCar.Models;
using Plugin.BLE;
using Plugin.BLE.Abstractions.Contracts;
using Plugin.BLE.Abstractions.EventArgs;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MauiCar.Services
{


    public class BluetoothLEService
    {
        public DeviceCandidate NewDeviceCandidateFromHomePage { get; set; } = new();
        public List<DeviceCandidate> DeviceCandidateList { get; private set; }
        public IBluetoothLE BluetoothLE { get; private set; }
        public IAdapter Adapter { get; private set; }
        public IDevice Device { get; set; }

        public BluetoothLEService()
        {
            BluetoothLE = CrossBluetoothLE.Current;
            Adapter = CrossBluetoothLE.Current.Adapter;
            Adapter.ScanTimeout = 4000;

            Adapter.DeviceDiscovered += Adapter_DeviceDiscovered;
            Adapter.DeviceConnected += Adapter_DeviceConnected;
       
        }

        private void Adapter_DeviceConnected(object sender, DeviceEventArgs e)
        {
            Debug.WriteLine($"Connect Ok");
            Device = e.Device;

        }

        public async Task<List<DeviceCandidate>> ScanForDevicesAsync()
        {
            DeviceCandidateList = new List<DeviceCandidate>();

            try
            {
                
                await Adapter.StartScanningForDevicesAsync();
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Unable to scan nearby Bluetooth LE devices: {ex.Message}.");
                await Shell.Current.DisplayAlert($"Unable to scan nearby Bluetooth LE devices", $"{ex.Message}.", "OK");
            }

            return DeviceCandidateList;
        }

        private  void Adapter_DeviceDiscovered(object sender, DeviceEventArgs e)
        {
            DeviceCandidate deviceCandidate = DeviceCandidateList.FirstOrDefault(d => d.Id == e.Device.Id);
            if (deviceCandidate == null)
            {
                DeviceCandidateList.Add(new DeviceCandidate
                {
                    Id = e.Device.Id,
                    Name = e.Device.Name,
                    Device=e.Device
                });
                Debug.WriteLine($"Found {e.Device.State.ToString().ToLower()} {e.Device.Name}.");
            }
        }


  








    }
}
