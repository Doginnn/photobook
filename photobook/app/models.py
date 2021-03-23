from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    image_url = models.ImageField("Imagem")
    description = models.CharField("Descrição da Foto", max_length=100, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Criada por")
    pub_date = models.DateField("Data de Publicação")

    def __str__(self):
        return self.name
