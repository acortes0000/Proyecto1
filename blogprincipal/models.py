from django.db import models
from django.utils import timezone

# Create your models in Blogprincipal
class blogprincipal(models.Model):
    detalles = models.CharField(max_length=1000, default='DEFAULT VALUE')
    logo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blogprincipal'