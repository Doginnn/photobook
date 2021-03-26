from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

from photobook.app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('upload_foto', views.upload_foto, name='upload_foto'),
    path('lista_foto', views.lista_foto, name='lista_foto'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
