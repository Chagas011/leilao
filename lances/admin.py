from django.contrib import admin
from .models import LancesVeiculo
# Register your models here.


@admin.register(LancesVeiculo)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['seu_lance', 'usuario_lance', 'lance_veiculo']
