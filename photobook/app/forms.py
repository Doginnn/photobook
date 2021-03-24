from django.forms import ModelForm
from photobook.app.models import Photo


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
