from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from jsonfield import JSONField

# Create your models here.

class Station(models.Model):
    NOAA = 'NOAA'
    OPNW = 'OPNW'

    STATION_SOURCE_CHOICES = [(NOAA, 'National Oceanic and Atmospheric Administration'),\
     (OPNW, 'OpenWeather')]

    data = JSONField()
    location = models.PointField(srid=4326, null=True, blank=True) 
    station_source = models.CharField(max_length=4, choices=STATION_SOURCE_CHOICES, default=NOAA)

    objects = models.GeoManager()
