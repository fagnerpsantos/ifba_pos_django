from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_chaves, name='listar_chaves'),
    path('cadastrar_chave', cadastrar_chave, name='cadastrar_chave'),
    path('editar_chave/<int:id>', editar_chave, name='editar_chave'),
    path('remover_chave/<int:id>', remover_chave, name='remover_chave'),
]
