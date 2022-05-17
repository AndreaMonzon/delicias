from django.db import models

# Create your models here.
from django.db import models
from distutils.command.upload import upload
# Create your models here.

class Categoria(models.Model):
    categoria= models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Productos(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    descripcion= models.TextField()
    categoria= models.ForeignKey(Categoria,on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos",null= True)

    def __str__(self):
        return self.nombre