from django.shortcuts import render, redirect, get_object_or_404
from photobook.app.models import Photo
from photobook.app.forms import PhotoForm
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


def lista_foto(request):
    form_lista_foto = Photo.objects.all().order_by('-id')
    context = {'form_lista_foto': form_lista_foto}
    return render(request, 'lista_foto.html', context)


def lista_foto_aprovada(request):
    form_lista_foto_aprovada = Photo.objects.filter(status=True)
    context = {'form_lista_foto_aprovada': form_lista_foto_aprovada}
    return render(request, 'lista_foto_aprovada.html', context)


def aprova_foto(request, pk):
    form_aprova_foto = get_object_or_404(Photo, pk=pk)
    form_aprova_foto.approve()
    return redirect('lista_foto_aprovada', pk=form_aprova_foto.upload.pk)


def deleta_foto(request, pk):
    form_deleta_foto = get_object_or_404(Photo, pk=pk)
    form_deleta_foto.approve()
    return redirect('lista_foto_aprovada', pk=form_deleta_foto.upload.pk)

# def deleta_foto(request, id):
#     foto = Photo.objects.get(id=id)
#     if request.method == 'POST':
#         foto.delete()
#         return redirect('fotos_aprovadas')
#     return render(request, 'deleta_foto.html', {'item': foto})
