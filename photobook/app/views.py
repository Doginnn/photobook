from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from photobook.app.models import Photo
from photobook.app.forms import PhotoForm


def base(request):
    form_base = User.objects.all()
    # return render(request, 'base.html', {'form_base': form_base})
    # return render(request, 'home.html', {'form_base': form_base})
    return render(request, 'upload_foto.html', {'form_base': form_base})


def lista_foto(request):
    form_lista_foto = Photo.objects.all()
    return render(request, 'lista_foto.html', {'form_lista_foto': form_lista_foto})


def upload_foto(request):
    if request.method == 'POST':
        form_upload_foto = PhotoForm(request.POST)
        if form_upload_foto.is_valid:
            form_upload_foto.save
            return redirect('base')
    else:
        form_upload_foto = PhotoForm()
    return render(request, 'upload_foto.html', {'form_upload_foto': form_upload_foto})


class PhotoCreateView(CreateView):
    model = Photo
    fields = ['upload']
    success_url = reverse_lazy('base')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = Photo.objects.all()
        context['photos'] = photos
        return context


def list_photo(request):
    pass


def aprove_photo(request):
    pass
