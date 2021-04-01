from django.shortcuts import render, redirect
from photobook.app.models import Photo
from photobook.app.forms import PhotoForm, AprovedForm
# from django.views.generic import


def home(request):
    form_home = Photo.objects.all()
    context = {'form_home': form_home}
    return render(request, 'base.html', context)


def upload_foto(request):
    if request.method == 'POST':
        form_upload_foto = PhotoForm(request.POST or None, request.FILES or None)
        context = {'form_upload_foto': form_upload_foto}
        if form_upload_foto.is_valid():
            form_upload_foto.save()
            return redirect('home')
    else:
        form_upload_foto = PhotoForm()
        context = {'form_upload_foto': form_upload_foto}
    return render(request, 'upload_foto.html', context)


# Função listando todas as fotos a serem aprovadas pelo ADMIN
def lista_foto(request):
    form_lista_foto = Photo.objects.all().order_by('-id')
    context = {'form_lista_foto': form_lista_foto}
    return render(request, 'lista_foto.html', context)


# Será um Carousel na HOME, abaixo do Carousel TOP 3.
def aprovar_fotos(request):
    form_aprovar_fotos = Photo.objects.all().filter('id','aprovado')
    context = {'form_aprovar_fotos': form_aprovar_fotos}
    return render(request, 'aprovar_fotos.html', context)


def deleta_foto(request, id):
    foto = Photo.objects.get(id=id)
    if request.method == 'POST':
        foto.delete()
        return redirect('fotos_aprovadas')
    return render(request, 'deleta_foto.html', {'item': foto})
