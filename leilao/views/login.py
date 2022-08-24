from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from leilao.forms import LoginForm


class Login(FormView):
    template_name = 'leilao/login.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'form': LoginForm(request.POST)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Dados invalidos')

        authenticated_user = authenticate(
            request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Logado com sucesso')
            login(request, authenticated_user)
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Usuario ou senha invalidos')

        return render(request, self.template_name, self.contexto)
