from django.db import models

# Create your models here.
class Libro (models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fechapublicacion = models.DateField(null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.title
