from django.db import models


# Create your models here.


class Biblicoteca(models.Model):
    nome_musica = models.CharField(max_length=100, null=False, blank=False)
    midia = models.FileField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.nome_musica
