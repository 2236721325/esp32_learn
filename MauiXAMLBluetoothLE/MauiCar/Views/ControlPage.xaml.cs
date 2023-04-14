using MauiCar.ViewModels;

namespace MauiCar.Views;

public partial class ControlPage : ContentPage
{
	public ControlPage(ControlPageViewModel vm)
	{
		InitializeComponent();
		BindingContext = vm;
	}
}