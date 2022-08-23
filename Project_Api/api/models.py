from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Cliente(models.Model):
    documento = models.IntegerField()
    tipo_documento = models.CharField(max_length=20, null=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Cliente")
    genero = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True)
    acceptance_tm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Tipo_tramite (models.Model):    
    descripcion_tipo = models.CharField(max_length=200,null=True,blank=True)
    nombre_tipo = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    