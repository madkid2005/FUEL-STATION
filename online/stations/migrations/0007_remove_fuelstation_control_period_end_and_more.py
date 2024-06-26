# Generated by Django 5.0.6 on 2024-06-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0006_remove_fuelstation_gas_tank1_stock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelstation',
            name='control_period_end',
        ),
        migrations.RemoveField(
            model_name='fuelstation',
            name='control_period_start',
        ),
        migrations.AddField(
            model_name='fuelstation',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ پایان دوره'),
        ),
        migrations.AddField(
            model_name='fuelstation',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ شروع دوره'),
        ),
    ]
