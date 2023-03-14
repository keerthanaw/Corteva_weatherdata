from django.conf import settings
from django.db import models
from django.db.models import Index

settings.configure(
    DEBUG=True,
)

#Create a new model Weather to inherit from the Model class in the models module
class Weather(models.Model):
    date = models.DateField(verbose_name='Date')
    station_id = models.CharField(max_length=10, verbose_name='Station ID')
    max_temperature = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Max Temperature')
    min_temperature = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Min Temperature')
    precipitation = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Precipitation')

    class Meta:
        indexes = [
            models.Index(fields=['date', 'station_id']),
        ]
