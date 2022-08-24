
from leilao.models import Veiculos
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from lances.models import LancesVeiculo
from lances.forms import FormLance
from django.contrib import messages


class LeilaoDetalhe(View):
    template_name = 'leilao/detalhe.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        pk = self.kwargs.get('pk')
        veiculo = get_object_or_404(Veiculos, pk=pk)

        self.contexto = {
            'veiculo': veiculo,
            'lances': LancesVeiculo.objects.filter(lance_veiculo=veiculo),
            'form': FormLance(request.POST)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']
        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        lance = form.save(commit=False)
        if request.user.is_authenticated:
            lance.usuario_lance = request.user

        lance.lance_veiculo = self.contexto['veiculo']
        lance.save()
        messages.success(self.request, 'Lance enviado com sucesso')
        return redirect('detalhe', pk=self.kwargs.get('pk'))
