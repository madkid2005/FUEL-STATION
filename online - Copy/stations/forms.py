from django import forms
from django.forms import inlineformset_factory
from .models import FuelStation, GasolineNozzle, GasNozzle, GasolineTank, GasTank

class FuelStationForm(forms.ModelForm):
    class Meta:
        model = FuelStation
        fields = [
            'name', 'gasoline_tanks', 'gasoline_nozzles', 'gas_tanks', 'gas_nozzles', 
            'control_period', 'product_type', 'gasoline_initial_stock', 'gasoline_received', 
            'gasoline_electronic_sales', 'gas_initial_stock', 'gas_received', 'gas_tank1_stock', 
            'gas_tank2_stock', 'diesel_electronic_sales'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'styled-input  allShow GazoiilShow GazShow'}),
            'gasoline_tanks': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow basehide allShow'}),
            'gasoline_nozzles': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow allShow'}),
            'gas_tanks': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'gas_nozzles': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'control_period': forms.TextInput(attrs={'class': 'styled-input  GazoiilShow GazShow basehide allShow'}),
            'product_type': forms.Select(attrs={'class': 'styled-input basehide allShow GazShow GazoiilShow'}),
            'gasoline_initial_stock': forms.NumberInput(attrs={'class': 'styled-input  GazoiilShow allShow'}),
            'gasoline_received': forms.NumberInput(attrs={'class': 'styled-input  GazoiilShow allShow'}),
            'gasoline_electronic_sales': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow allShow'}),
            'gas_initial_stock': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'gas_received': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'gas_tank1_stock': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'gas_tank2_stock': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'diesel_electronic_sales': forms.NumberInput(attrs={'class': 'styled-input GazShow basehide allShow GazoiilShow'}),
        }

class GasolineNozzleForm(forms.ModelForm):
    class Meta:
        model = GasolineNozzle
        fields = ['nozzle_number', 'totalizer_start', 'totalizer_end']
        widgets = {
            'nozzle_number': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow allShow'}),
            'totalizer_start': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow allShow'}),
            'totalizer_end': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow allShow'}),
        }

class GasNozzleForm(forms.ModelForm):
    class Meta:
        model = GasNozzle
        fields = ['nozzle_number', 'totalizer_start', 'totalizer_end']
        widgets = {
            'nozzle_number': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'totalizer_start': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'totalizer_end': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
        }

class GasolineTankForm(forms.ModelForm):
    class Meta:
        model = GasolineTank
        fields = ['tank_number', 'final_stock']
        widgets = {
            'tank_number': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow'}),
            'final_stock': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow'}),
        }

class GasTankForm(forms.ModelForm):
    class Meta:
        model = GasTank
        fields = ['tank_number', 'final_stock']
        widgets = {
            'tank_number': forms.NumberInput(attrs={'class': 'styled-input GazShow'}),
            'final_stock': forms.NumberInput(attrs={'class': 'styled-input GazShow'}),
        }

# Nozzles
GasolineNozzleFormSet = inlineformset_factory(FuelStation, GasolineNozzle, form=GasolineNozzleForm, extra=12)
GasNozzleFormSet = inlineformset_factory(FuelStation, GasNozzle, form=GasNozzleForm, extra=12)

# Tanks
GasolineTankFormSet = inlineformset_factory(FuelStation, GasolineTank, form=GasolineTankForm, extra=0)
GasTankFormSet = inlineformset_factory(FuelStation, GasTank, form=GasTankForm, extra=0)
