from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_chaves, name='listar_chaves'),
    path('cadastrar_chave', cadastrar_chave, name='cadastrar_chave'),
    path('editar_chave/<int:id>', editar_chave, name='editar_chave'),
    path('remover_chave/<int:id>', remover_chave, name='remover_chave'),
    path('cadastrar_usuario', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario', deslogar_usuario, name='deslogar_usuario'),

]
