
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils.validador_cpf import valida_cpf

from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11)

    def clean(self):
        error_messages = {}

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF valido'
        if error_messages:
            raise ValidationError(error_messages)

    def __str__(self) -> str:
        return f'{self.usuario.first_name} {self.usuario.last_name}'


@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def salvar_perfil(sender, instance, **kwargs):
    instance.perfil.save()
