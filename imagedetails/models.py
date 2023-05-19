from django import forms
from django.db import models
from django.core.exceptions import ValidationError

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    image_data = models.BinaryField(blank = True, null = True, editable=True)
    
    class Meta:
        db_table="image"

