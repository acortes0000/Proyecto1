from django.db import models
from django.utils import timezone

# Create your models in Usuarios
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField()
    mail = models.CharField(max_length=50, default='DEFAULT VALUE')
    descripcion = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'