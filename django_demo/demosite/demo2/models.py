from django.db import models

# Create your models here.

class Location(models.Model):
    id_location = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20, blank=True, null=True)

class Travel(models.Model):
    id_travel = models.IntegerField(primary_key=True)
    target = models.CharField(max_length=100)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    companion = models.CharField(max_length=100)
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)