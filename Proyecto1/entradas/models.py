from django.db import models
from django.utils import timezone

# Create your models in Entradas
class Entradas(models.Model):
    titulos = models.CharField(max_length=100, default='DEFAULT VALUE')
    contenido = models.TextField(default='DEFAULT VALUE')
    img = models.FileField()
    slug = models.CharField(max_length=5000, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'entradas'