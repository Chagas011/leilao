from django.urls import path

from . import views


urlpatterns = [
    path('<int:pk>', views.PerfilView.as_view(), name='perfil'),
    path('update/<int:pk>', views.PerfilUpdate.as_view(), name='perfil_update')
]
