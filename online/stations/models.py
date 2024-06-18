from django.db import models

class FuelStation(models.Model):
    name = models.CharField('اسم جایگاه',max_length=255) # اسم جایگاه
    
    gasoline_tanks = models.PositiveIntegerField('تعداد مخزن های بنزین',default=0, null=True, blank=True) # تعداد مخزن های بنزین
    gasoline_nozzles = models.PositiveIntegerField('تعداد نازل های بنزین',default=0, null=True, blank=True) # تعداد نازل های بنزین
    
    gas_tanks = models.PositiveIntegerField('تعداد مخازن گاز',default=0) # تعداد مخازن گاز
    gas_nozzles = models.PositiveIntegerField('تعداد نازل های گاز',default=0, null=True, blank=True)  # تعداد نازل های گاز
    
    control_period = models.CharField('انتخاب دوره',max_length=50, choices=[('start', 'ابتدا دوره'), ('end', 'انتهای دوره')])  # انتخاب دوره
    start_date = models.DateField('تاریخ شروع دوره', blank=True, null=True)
    end_date = models.DateField('تاریخ پایان دوره', blank=True, null=True)
    
    product_type = models.CharField('انتخاب محصول',max_length=50, choices=[('gasoline', 'بنزین'), ('diesel', 'نفتگاز'), ('both', 'هر دو')])  # انتخاب محصول
    
    # Gasoline fields
    gasoline_initial_stock = models.PositiveIntegerField('موجودی اول دوره بنزین',null=True, blank=True) # موجودی اول دوره بنزین
    gasoline_received = models.PositiveIntegerField('مقدار رسیده دوره بنزین',null=True, blank=True)   # مقدار رسیده دوره بنزین
    
    gasoline_electronic_samane_sales = models.PositiveIntegerField('مقدار فروش الکترونیکی سامانه بنزین',null=True, blank=True) # مقدار فروش الکترونیکی بنزین
    gasoline_electronic_sales = models.PositiveIntegerField('مقدار فروش الکترونیکی بنزین',null=True, blank=True) # مقدار فروش الکترونیکی بنزین
    
    gasoline_final_stock = models.FloatField('موجودی انتهای دوره بنزین',null=True, blank=True)   # موجودی انتهای دوره بنزین

    # Diesel fields
    gas_initial_stock = models.PositiveIntegerField('موجودی اول دوره گاز',null=True, blank=True) # موجودی اول دوره گاز
    gas_received = models.PositiveIntegerField('مقدار رسیده دوره گاز',null=True, blank=True)   # مقدار رسیده دوره گاز
    
    diesel_electronic_samane_sales = models.PositiveIntegerField('مقدار فروش الکترونیکی سامانه گاز',null=True, blank=True)  # مقدار فروش الکترونیکی گاز
    diesel_electronic_sales = models.PositiveIntegerField('مقدار فروش الکترونیکی گاز',null=True, blank=True)  # مقدار فروش الکترونیکی گاز
    
    gas_final_stock = models.FloatField('موجودی انتهای دوره گاز',null=True, blank=True) # موجودی انتهای دوره گاز

    def __str__(self):
        return self.name



# نازل های بنزین
class GasolineNozzle(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE, related_name='gasoline_nozzles_details')
    nozzle_number = models.PositiveIntegerField() # شماره نازل
    totalizer_start = models.PositiveIntegerField() # عدد ابتدا دوره نازل
    totalizer_end = models.PositiveIntegerField()  # عدد انتها دوره نازل

    def __str__(self):
        return f'{self.station.name} - Nozzle {self.nozzle_number}'



# نازل های گاز
class GasNozzle(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE, related_name='gas_nozzles_details')
    nozzle_number = models.PositiveIntegerField() # شماره نازل
    totalizer_start = models.PositiveIntegerField() # عدد ابتدا دوره نازل
    totalizer_end = models.PositiveIntegerField() # عدد انتها دوره نازل

    def __str__(self):
        return f'{self.station.name} - Nozzle {self.nozzle_number}'


# مخزن های بنزین
class GasolineTank(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    tank_number = models.IntegerField() # شماره مخزن
    final_stock = models.FloatField() # موجودی مخزن'

# مخزن های گاز
class GasTank(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    tank_number = models.IntegerField() # شماره مخزن
    final_stock = models.FloatField() # موجودی مخزن'