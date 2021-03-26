from django.db import models


class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.ImageField()
    description = models.CharField("Descrição da Foto", max_length=100, blank=True)

    def __str__(self):
        return self.description
