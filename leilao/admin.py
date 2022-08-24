from django.contrib import admin
from .models import Veiculos

# Register your models here.


class VeiculosAdmin(admin.ModelAdmin):
    list_display = ['nome_veiculo', 'marca_veiculo',
                    'ano_veiculo', 'preco_veiculo', 'preco_tabela']


admin.site.register(Veiculos, VeiculosAdmin)
