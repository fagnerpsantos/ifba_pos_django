from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import Chave
from .forms import ChaveForm

# Create your views here.

def listar_chaves(request):
    chaves = Chave.objects.all()
    return render(request, 'chaves/index.html', {'chaves': chaves})

@login_required()
def cadastrar_chave(request):
    if request.method == "POST":
        form_chave = ChaveForm(request.POST)
        if form_chave.is_valid():
            form_chave.save()
            return redirect('listar_chaves')
    else:
        form_chave = ChaveForm()
    return render(request, 'chaves/form_chave.html', {'form_chave': form_chave})

@login_required()
def editar_chave(request, id):
    chave_bd = Chave.objects.get(id=id)
    form_chave = ChaveForm(request.POST or None, instance=chave_bd)

    if form_chave.is_valid():
        form_chave.save()
        return redirect('listar_chaves')
    return render(request, 'chaves/form_chave.html', {'form_chave': form_chave})

@login_required()
def remover_chave(request, id):
    chave = Chave.objects.get(id=id)
    if request.method == "POST":
        chave.delete()
        return redirect('listar_chaves')
    return render(request, 'chaves/confirma_exclusao.html', {'chave': chave})


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_chaves')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('listar_chaves')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form_login': form_login})

def deslogar_usuario(request):
    logout(request)

    return redirect('listar_chaves')