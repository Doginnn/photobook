from django.contrib import admin
from photobook.app.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'upload', 'description', 'uploaded_at']
