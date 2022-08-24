from django.views.generic import ListView
from leilao.models import Veiculos


class LeilaoIndex(ListView):
    model = Veiculos
    template_name = 'leilao/index.html'
    paginate_by = 6
    context_object_name = 'veiculos'
