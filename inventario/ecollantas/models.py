from django.db import models

# Create your models here.
GARANTIA=(
    ('1','Si'),
    ('2','No'),
)


class Categoria(models.Model):
    tipo= models.CharField(max_length=30, unique=True)

class Marca(models.Model):
    tipo: models.CharField(max_length=30, unique=True)

class Rin(models.Model):
    tipo: models.CharField(max_length=30, unique=True)
    
class productos(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    rin = models.ForeignKey(Rin, on_delete = models.CASCADE)
    marca = models.CharField(max_length=20)
    referencia = models.CharField(max_length=30)
    garantia = models.CharField(max_length=30, null=True,choices=GARANTIA)
    descripcion = models.CharField(max_length=250)
    precio = models.FloatField()
    