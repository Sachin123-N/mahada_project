from django import forms
from .models import Maha


class MahaForm(forms.ModelForm):
    class Meta:
        model = Maha
        fields = "__all__"

    widgets = {
        'plot_name': forms.TextInput(attrs={'class': 'form-control'}),
        'plot_area': forms.NumberInput(attrs={'class': 'form-control'}),
        'plot_price': forms.NumberInput(attrs={'class': 'form-control'}),
        'payment_mode': forms.Select(attrs={'class': 'form-control'}),
    }