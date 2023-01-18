from django.shortcuts import render
from .models import Produto

def index(request):

    produtos = Produto.objects.all()
    context = {
        'curso': 'Django Framework',
        'nome': 'Rafael',
        'produtos': produtos,
    }
    return render(request, "index.html", context)

def contact(request):
    return render(request, "contact.html")

def produto(request, params):

    prod = Produto.objects.get(id=params)
    context = {
        'produto': prod,
    }
    return render(request, "produto.html", context)
