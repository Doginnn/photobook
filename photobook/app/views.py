from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'
