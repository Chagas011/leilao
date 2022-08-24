from django.db import models
from django.contrib.auth.models import User
from leilao.models import Veiculos
# Create your models here.


class LancesVeiculo(models.Model):
    seu_lance = models.CharField(max_length=100, blank=True, null=True)
    lance_veiculo = models.ForeignKey(
        Veiculos, on_delete=models.CASCADE
    )
    usuario_lance = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Usuario'
    )

    def __str__(self):
        return self.seu_lance
