from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from photobook.app.models import Photo


def base(request):
    form_base = User.objects.all()
    # return render(request, 'base.html', {'form_base': form_base})
    # return render(request, 'home.html', {'form_base': form_base})
    return render(request, 'photo_form.html', {'form_base': form_base})


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
