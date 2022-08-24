from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from .models import Perfil
from django.urls import reverse_lazy


class PerfilView(TemplateView):
    template_name = 'perfil/perfil.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        perfil_id = context.get('pk')
        perfil = get_object_or_404(Perfil.objects.filter(pk=perfil_id))

        return self.render_to_response({
            **context,
            'perfil': perfil,
        })


@method_decorator(
    login_required(
        login_url='login', redirect_field_name='next'), name='dispatch')
class PerfilUpdate(UpdateView):
    template_name = 'perfil/perfil_update.html'
    model = Perfil
    fields = ['data_nascimento', 'cpf']
    success_url = reverse_lazy('index')
    context_object_name = 'perfil'
