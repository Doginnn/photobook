from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.ImageField("Foto", null=True, blank=True)
    description = models.CharField("Descrição da Foto", max_length=100)
    status = models.BooleanField("Status", default=False, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Selecione um Usuário")

    def approve(self):
        self.status = True
        self.save()

    def __str__(self):
        return self.description
