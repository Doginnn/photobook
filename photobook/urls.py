from django.contrib import admin
from django.urls import path

from photobook.app import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
