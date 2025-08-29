from django.db import models

# Create your models here.

# class Autor (models.Model):
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     fecha_nacimiento = models.DateField(null=True, blank=True)
#     nacionalidad = models.CharField(max_length=50, null=True, blank=True)
    
#     def __str__(self):
#         return self.nombre + " " + self.apellido

class Libro (models.Model):
    titulo = models.CharField(max_length=200)
    fechapublicacion = models.DateField(null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    autor = models.CharField(max_length=200)


    def __str__(self):
        return self.titulo
