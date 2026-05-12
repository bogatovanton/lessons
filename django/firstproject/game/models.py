from django.db import models

# Create your models here.
class Events(models.Model):
    id = models.IntegerField(verbose_name="ID", unique=True, primary_key=True)
    title = models.CharField(verbose_name="Название", max_length=50)
    date = models.DateField(verbose_name="Дата")
    location = models.CharField(verbose_name="Локация", max_length=50)