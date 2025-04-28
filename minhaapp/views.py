from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.shortcuts import get_object_or_404, redirect

def lista_produtos(request):
    produtos = Produto.objects.all()

    return render(request, 'minhaapp/lista_produtos.html', {'produtos': produtos})

def detalhe_produto(request, produto_id):

    produto = Produto.objects.get(id=produto_id)

    return render(request, 'minhaapp/detalhe_produto.html', {'produto': produto})

def remover_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto removido com sucesso!')
        return redirect('lista_produtos')

    return render(request, 'minhaapp/confirmar_remocao.html', {'produto': produto})



def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    
    return render(request, 'minhaapp/cadastro_produto.html', {'form': form})

def home(request):
    return render(request, 'minhaapp/base.html')