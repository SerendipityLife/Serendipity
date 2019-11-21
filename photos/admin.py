from django.contrib import admin
from . import models

@admin.register(models.Photo)
class CustomPhoto(admin.ModelAdmin):
    pass

@admin.register(models.Photo_info)
class CustomPhotoInfo(admin.ModelAdmin):
    pass