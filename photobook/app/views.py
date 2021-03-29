from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from photobook.app.models import Photo
from photobook.app.forms import PhotoForm


def home(request):
    form_home = Photo.objects.all()
    return render(request, 'base.html', {'form_home': form_home})


def lista_foto(request):
    form_lista_foto = Photo.objects.all()
    return render(request, 'lista_foto.html', {'form_lista_foto': form_lista_foto})


def upload_foto(request):
    if request.method == 'POST':
        form_upload_foto = PhotoForm(request.POST or None, request.FILES or None)
        if form_upload_foto.is_valid():
            form_upload_foto.save()
            messages.success(request, "Upload realizado com SUCESSO!")
            return redirect('lista_foto')
    else:
        form_upload_foto = PhotoForm()
    return render(request, 'upload_foto.html', {'form_upload_foto': form_upload_foto})


def aprovar_foto(request):
    pass


def deletar_foto(request):
    pass


# class PhotoCreateView(CreateView):
#     model = Photo
#     fields = ['upload']
#     success_url = reverse_lazy('base')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         photos = Photo.objects.all()
#         context['photos'] = photos
#         return context
