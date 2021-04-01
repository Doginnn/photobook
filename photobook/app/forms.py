from django import forms
from photobook.app.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['upload','description','user']


class AprovedForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['aprovado']
