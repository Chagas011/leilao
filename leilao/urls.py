from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeilaoIndex.as_view(), name='index'),
    path('leilao/<str:categoria>/',
         views.CategoriaLeilao.as_view(),
         name='categoria'
         ),
    path('cadastro', views.Cadastro.as_view(), name='cadastro'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('detalhes/<int:pk>', views.LeilaoDetalhe.as_view(), name='detalhe'),
    path('atendimento', views.Atendimento.as_view(), name='atendimento'),
    path('empresa', views.Empresa.as_view(), name='sobre_nos'),
]
