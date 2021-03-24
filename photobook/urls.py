from django.contrib import admin
from django.urls import path

from photobook.app import views


urlpatterns = [
    path('', views.base),
    path('admin/', admin.site.urls),
]
