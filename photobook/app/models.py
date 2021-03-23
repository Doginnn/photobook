from django.db import models


class Photo(models.Model):
    name = models.CharField("Nome da Foto: ", max_length=100)
    description = models.CharField("Descrição da Foto: ", max_length=100, null=True)
    pub_date = models.DateField("Data de Publicação:")
    status = models.BooleanField("Status")

    def __str__(self):
        return self.name
