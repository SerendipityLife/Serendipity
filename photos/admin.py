from django.contrib import admin
from django.utils.html import mark_safe
from . import models

@admin.register(models.Photo)
class CustomPhoto(admin.ModelAdmin):

    """ Custom Photo Admin """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        print(obj.photo)
        return mark_safe(f'<img src="{obj.photo.url}" />')

    get_thumbnail.short_description = "Thumbnail"

@admin.register(models.Photo_info)
class CustomPhotoInfo(admin.ModelAdmin):

    pass