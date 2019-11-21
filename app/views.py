from django.shortcuts import render, redirect
from .models import Chave
from .forms import ChaveForm

# Create your views here.

def listar_chaves(request):
    chaves = Chave.objects.all()
    return render(request, 'chaves/index.html', {'chaves': chaves})

def cadastrar_chave(request):
    if request.method == "POST":
        form_chave = ChaveForm(request.POST)
        if form_chave.is_valid():
            form_chave.save()
            return redirect('listar_chaves')
    else:
        form_chave = ChaveForm()
    return render(request, 'chaves/form_chave.html', {'form_chave': form_chave})

def editar_chave(request, id):
    chave_bd = Chave.objects.get(id=id)
    form_chave = ChaveForm(request.POST or None, instance=chave_bd)

    if form_chave.is_valid():
        form_chave.save()
        return redirect('listar_chaves')
    return render(request, 'chaves/form_chave.html', {'form_chave': form_chave})

def remover_chave(request, id):
    chave = Chave.objects.get(id=id)
    if request.method == "POST":
        chave.delete()
        return redirect('listar_chaves')
    return render(request, 'chaves/confirma_exclusao.html', {'chave': chave})