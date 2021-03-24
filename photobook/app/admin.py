from django.contrib import admin
from photobook.app.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_url', 'description', 'created_by', 'pub_date']
