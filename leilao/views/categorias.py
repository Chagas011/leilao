from .index import LeilaoIndex


class CategoriaLeilao(LeilaoIndex):
    template_name = 'leilao/categorias.html'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria')
        if not categoria:
            return qs

        qs = qs.filter(categoria_veiculo__nome_categoria__iexact=categoria)
        return qs
