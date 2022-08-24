from categorias.models import Categoria
from django.db import models
from PIL import Image
from django.conf import settings
import os
# Create your models here.


class Veiculos(models.Model):
    nome_veiculo = models.CharField(max_length=75, verbose_name='Nome')
    marca_veiculo = models.CharField(max_length=75, verbose_name='Marca')
    ano_veiculo = models.DateField()
    preco_veiculo = models.CharField(max_length=155, verbose_name='Preco')
    preco_tabela = models.CharField(
        max_length=155, verbose_name='Preco Tabela')
    estado_veiculo = models.CharField(
        max_length=50, verbose_name='Estado veiculo')
    descricao_curta_veiculo = models.CharField(
        max_length=50, verbose_name='Descricao')
    descricao_veiculo = models.TextField(verbose_name='Descricao')
    imagem = models.ImageField(
        upload_to='img/%Y/%m',
        blank=True, null=True, verbose_name='Imagem')
    categoria_veiculo = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        blank=True, null=True, verbose_name='Categoria'
    )

    inicio_lance = models.DateField(
        blank=True, null=True
    )

    final_lance = models.DateField(
        blank=True, null=True
    )

    def resize_image(self, img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_heigth = img_pil.size

        if original_width >= new_width:
            new_heigth = round((new_width * original_heigth) / original_width)
            new_img = img_pil.resize((new_width, new_heigth), Image.LANCZOS)
            new_img.save(
                img_full_path,
                optimize=True,
                quality=50
            )
            return new_img
        else:
            return img_pil.close()

    def __str__(self) -> str:
        return self.nome_veiculo

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
