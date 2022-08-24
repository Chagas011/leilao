from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from leilao.forms import CadastroForm
from perfil.models import Perfil


class Cadastro(FormView):
    template_name = 'leilao/cadastro.html'
    cpf_perfil = Perfil.cpf

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'form': CadastroForm(request.POST)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = CadastroForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        user = form.save(commit=False)

        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuario criado com sucesso')
        return redirect(reverse('login'))
