from django.contrib import admin
from .models import Image

class Image_admin(admin.ModelAdmin):
    list_display = ["title","description", "image","category","image_data"]

admin.site.register(Image, Image_admin)