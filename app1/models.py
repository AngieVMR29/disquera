from django.db import models

# Create your models here.

class Disquera(models.Model):
    id=models.AutoField(primary_key=True)
    nitdisquera=models.CharField(max_length=25)
    nombredisquera=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    direccion=models.CharField(max_length=100)
    estadoDisquera=models.BooleanField()
    
class Artista(models.Model):
    id=models.AutoField(primary_key=True)
    iddisquerakf= models.ForeignKey(Disquera,on_delete=models.CASCADE)
    