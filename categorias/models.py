
from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=75, verbose_name='Categoria')

    def __str__(self) -> str:
        return self.nome_categoria
