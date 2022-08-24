from django.forms import ModelForm
from lances.models import LancesVeiculo


class FormLance(ModelForm):
    class Meta:
        model = LancesVeiculo
        fields = ('seu_lance',)
