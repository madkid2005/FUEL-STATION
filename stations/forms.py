from django import forms
from django.forms import inlineformset_factory
from .models import FuelStation, GasolineNozzle, GasNozzle

class FuelStationForm(forms.ModelForm):
    class Meta:
        model = FuelStation
        fields = ['name', 'gasoline_tanks', 'gasoline_nozzles', 'gas_tanks', 'gas_nozzles', 'control_period', 'product_type',
                  'gasoline_initial_stock', 'gasoline_received', 'gasoline_tank1_stock', 'gasoline_tank2_stock', 'gasoline_electronic_sales',
                  'gas_initial_stock', 'gas_received', 'gas_tank1_stock', 'gas_tank2_stock', 'diesel_electronic_sales']

class GasolineNozzleForm(forms.ModelForm):
    class Meta:
        model = GasolineNozzle
        fields = ['nozzle_number', 'totalizer_start', 'totalizer_end']

class GasNozzleForm(forms.ModelForm):
    class Meta:
        model = GasNozzle
        fields = ['nozzle_number', 'totalizer_start', 'totalizer_end']

GasolineNozzleFormSet = inlineformset_factory(FuelStation, GasolineNozzle, form=GasolineNozzleForm, extra=12)
GasNozzleFormSet = inlineformset_factory(FuelStation, GasNozzle, form=GasNozzleForm, extra=12)
