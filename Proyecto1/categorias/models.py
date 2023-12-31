from django.db import models

from django.utils import timezone

# Create your models in Categorias
class Categorias(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    detalles = models.CharField(max_length=1000, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categorias'