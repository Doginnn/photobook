from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

from photobook.app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('upload_foto', views.upload_foto, name='upload_foto'),
    path('lista_foto_aprovada', views.lista_foto_aprovada, name='lista_foto_aprovada'),
    path('aprova_foto', views.aprova_foto, name='aprova_foto'),
    path('admin/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
