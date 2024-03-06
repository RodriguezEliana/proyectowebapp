from django.db import models

# Create your models here.
class equipo(models.Model):
    id= models.AutoField(primary_key=True)
    equipo= models.CharField(max_length=100, verbose_name="Equipo")
    descripción =models.TextField(verbose_name="Descripción", null=True)