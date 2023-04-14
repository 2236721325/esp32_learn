using MauiCar.Models;
using MauiCar.ViewModels;
using System.Diagnostics;

namespace MauiCar.Views;

public partial class ScanPage : ContentPage
{
	private readonly ScanPageViewModel _vm;
	public ScanPage(ScanPageViewModel vm)
	{
		InitializeComponent();
		BindingContext = vm;
		_vm = vm;
	}

    private async void ListView_ItemTapped(object sender, ItemTappedEventArgs e)
    {
		 await _vm.ConnectToDeviceAsync(e.Item as DeviceCandidate);
    }
}