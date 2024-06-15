from django.db import models

class FuelStation(models.Model):
    name = models.CharField(max_length=255) # اسم جایگاه
    gasoline_tanks = models.PositiveIntegerField(default=0) # تعداد مخزن های بنزین
    gasoline_nozzles = models.PositiveIntegerField(default=0, null=True, blank=True) # تعداد نازل های بنزین
    gas_tanks = models.PositiveIntegerField(default=0) # تعداد 
    gas_nozzles = models.PositiveIntegerField(default=0, null=True, blank=True)
    control_period = models.CharField(max_length=50, choices=[('start', 'ابتدا دوره'), ('end', 'انتهای دوره')])
    product_type = models.CharField(max_length=50, choices=[('gasoline', 'بنزین'), ('diesel', 'نفتگاز'), ('both', 'هر دو')])
    
    # Gasoline fields
    gasoline_initial_stock = models.PositiveIntegerField(null=True, blank=True)
    gasoline_received = models.PositiveIntegerField(null=True, blank=True)
    gasoline_tank1_stock = models.PositiveIntegerField(null=True, blank=True)
    gasoline_tank2_stock = models.PositiveIntegerField(null=True, blank=True)
    gasoline_electronic_sales = models.PositiveIntegerField(null=True, blank=True)
    gasoline_final_stock = models.FloatField(null=True, blank=True)

    # Diesel fields
    gas_initial_stock = models.PositiveIntegerField(null=True, blank=True)
    gas_received = models.PositiveIntegerField(null=True, blank=True)
    gas_tank1_stock = models.PositiveIntegerField(null=True, blank=True)
    gas_tank2_stock = models.PositiveIntegerField(null=True, blank=True)
    diesel_electronic_sales = models.PositiveIntegerField(null=True, blank=True)
    gas_final_stock = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name



# نازل های بنزین
class GasolineNozzle(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE, related_name='gasoline_nozzles_details')
    nozzle_number = models.PositiveIntegerField()
    totalizer_start = models.PositiveIntegerField()
    totalizer_end = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.station.name} - Nozzle {self.nozzle_number}'



# نازل های گاز
class GasNozzle(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE, related_name='gas_nozzles_details')
    nozzle_number = models.PositiveIntegerField()
    totalizer_start = models.PositiveIntegerField()
    totalizer_end = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.station.name} - Nozzle {self.nozzle_number}'


# مخزن های بنزین
class GasolineTank(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    tank_number = models.IntegerField()
    final_stock = models.FloatField()

# مخزن های گاز
class GasTank(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    tank_number = models.IntegerField()
    final_stock = models.FloatField()