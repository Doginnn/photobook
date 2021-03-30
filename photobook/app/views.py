from django.shortcuts import render, redirect
from photobook.app.models import Photo
from photobook.app.forms import PhotoForm


def home(request):
    form_home = Photo.objects.all()
    return render(request, 'base.html', {'form_home': form_home})


def lista_foto(request):
    form_lista_foto = Photo.objects.all()
    return render(request, 'lista_foto.html', {'form_lista_foto': form_lista_foto})


def fotos_aprovadas(request):
    form_fotos_aprovadas = Photo.objects.all()
    return render(request, 'fotos_aprovadas.html', {'form_fotos_aprovadas': form_fotos_aprovadas})


def upload_foto(request):
    if request.method == 'POST':
        form_upload_foto = PhotoForm(request.POST or None, request.FILES or None)
        if form_upload_foto.is_valid():
            form_upload_foto.save()
            return redirect('lista_foto')
    else:
        form_upload_foto = PhotoForm()
    return render(request, 'upload_foto.html', {'form_upload_foto': form_upload_foto})


def aprova_foto(request, pk):
    if request.method == 'POST':
        order = Photo.objects.get(id=pk)
        form_aprova_foto = PhotoForm(request.POST, instance=order)
        if form_aprova_foto.is_valid():
            form_aprova_foto.save()
            return redirect('fotos_aprovadas')
    else:
        form_aprova_foto = PhotoForm()
    return render(request, 'aprova_foto.html', {'form_aprova_foto': form_aprova_foto})


def deleta_foto(request, id):
    foto = Photo.objects.get(id=id)
    if request.method == 'POST':
        foto.delete()
        return redirect('fotos_aprovadas')
    return render(request, 'deleta_foto.html', {'item': foto})

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
