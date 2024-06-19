from django import forms
from django.forms import inlineformset_factory
from .models import FuelStation, GasolineNozzle, GasNozzle, GasolineTank, GasTank

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class FuelStationForm(forms.ModelForm):
    
    class Meta:
        
        model = FuelStation
        
        fields = ['name', 'gasoline_tanks', 'gasoline_nozzles', 'gas_tanks', 'gas_nozzles', 'control_period',
                  'start_date', 'end_date', 'product_type',
                  'gasoline_initial_stock', 'gasoline_received', 'gasoline_electronic_sales','gasoline_electronic_samane_sales',
                  'gas_initial_stock', 'gas_received', 'diesel_electronic_sales', 'diesel_electronic_samane_sales',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'styled-input  allShow GazoiilShow GazShow'}),
            'gasoline_tanks': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow basehide allShow'}),
            'gasoline_nozzles': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow allShow'}),
            'gas_tanks': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'gas_nozzles': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'control_period': forms.Select(attrs={'class': 'styled-input  GazoiilShow GazShow basehide allShow'}),
            'product_type': forms.Select(attrs={'class': 'styled-input basehide allShow GazShow GazoiilShow'}),
            'gasoline_initial_stock': forms.NumberInput(attrs={'class': 'styled-input  GazoiilShow allShow'}),
            'gasoline_received': forms.NumberInput(attrs={'class': 'styled-input  GazoiilShow allShow'}),
            'gasoline_electronic_sales': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow allShow'}),
            'gas_initial_stock': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'gas_received': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'gas_tank1_stock': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'gas_tank2_stock': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'diesel_electronic_sales': forms.NumberInput(attrs={'class': 'styled-input GazShow basehide allShow GazoiilShow'}),
            'diesel_electronic_samane_sales': forms.NumberInput(attrs={'class': 'styled-input GazShow basehide allShow GazoiilShow'}),
            'gasoline_electronic_samane_sales': forms.NumberInput(attrs={'class': 'styled-input GazShow basehide  allShow GazoiilShow'}),
            'end_date': forms.NumberInput(attrs={'class': 'styled-input GazShow basehide allShow GazoiilShow'}),
            'start_date': forms.NumberInput(attrs={'class': 'styled-input GazShow basehide allShow GazoiilShow'}),
        }

        labels = {
            'name': 'نام',
            'gasoline_tanks': 'تعداد مخازن بنزین',
            'gasoline_nozzles': 'تعداد نازل‌های بنزین',
            'gas_tanks': 'تعداد مخازن گاز',
            'gas_nozzles': 'تعداد نازل‌های گاز',
            'control_period': 'دوره کنترل',
            'start_date' : 'تاریخ شروع',
            'end_date' : 'تاریخ پایان',
            'product_type': 'نوع محصول',
            'gasoline_initial_stock': 'موجودی اولیه بنزین',
            'gasoline_received': 'بنزین دریافتی',
            'gasoline_electronic_sales': 'فروش الکترونیکی بنزین',
            'gasoline_electronic_samane_sales': 'فروش الکترونیکی سامانه بنزین',
            'gas_initial_stock': 'موجودی اولیه گاز',
            'gas_received': 'گاز دریافتی',
            'diesel_electronic_sales': 'فروش الکترونیکی گازوئیل',
            'diesel_electronic_samane_sales': 'فروش الکترونیکی سامانه گازوئیل',
        }


        
        
class GasolineNozzleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GasolineNozzleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('nozzle_number', css_class='form-control'),
            Field('totalizer_start', css_class='form-control'),
            Field('totalizer_end', css_class='form-control'),
        )

    class Meta:
        model = GasolineNozzle
        fields = ['nozzle_number', 'totalizer_start', 'totalizer_end']
        labels = {
            'nozzle_number': 'شماره نازل',
            'totalizer_start': 'شروع توتالایزر',
            'totalizer_end': 'پایان توتالایزر',
        }

class GasNozzleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GasNozzleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('nozzle_number', css_class='form-control'),
            Field('totalizer_start', css_class='form-control'),
            Field('totalizer_end', css_class='form-control'),
        )

    class Meta:
        model = GasNozzle
        fields = ['nozzle_number', 'totalizer_start', 'totalizer_end']
        labels = {
            'nozzle_number': 'شماره نازل',
            'totalizer_start': 'شروع توتالایزر',
            'totalizer_end': 'پایان توتالایزر',
        }
      
        
 
class GasolineTankForm(forms.ModelForm):
    class Meta:
        model = GasolineTank
        fields = ['tank_number', 'final_stock']
        widgets = {
            'tank_number': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow allShow basehide'}),
            'final_stock': forms.NumberInput(attrs={'class': 'styled-input GazoiilShow allShow basehide'}),
        }
 
        labels = {
            'tank_number': 'شماره مخزن',
            'final_stock': 'موجودی مخزن',
        }
        
class GasTankForm(forms.ModelForm):
    class Meta:
        model = GasTank
        fields = ['tank_number', 'final_stock']
        widgets = {
            'tank_number': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
            'final_stock': forms.NumberInput(attrs={'class': 'styled-input GazShow allShow'}),
        }
        
        
        labels = {
            'tank_number': 'شماره مخزن',
            'final_stock': 'موجودی مخزن',
        }
# nozzles
GasolineNozzleFormSet = inlineformset_factory(FuelStation, GasolineNozzle, form=GasolineNozzleForm, extra=12)
GasNozzleFormSet = inlineformset_factory(FuelStation, GasNozzle, form=GasNozzleForm, extra=12)

# tanks
GasolineTankFormSet = inlineformset_factory(FuelStation, GasolineTank, form=GasolineTankForm, extra=0)
GasTankFormSet = inlineformset_factory(FuelStation, GasTank, form=GasTankForm, extra=0)