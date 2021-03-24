from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView


def base(request):
    form_base = User.objects.all()
    return render(request, 'base.html', {'form_base': form_base})


def upload_photo(request):
    pass


def list_photo(request):
    pass


def aprove_photo(request):
    pass
