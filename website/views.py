from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def products(request, id):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def contact(request):
    return render(request, 'contact.html')

# def login(request):
#     return render(request, 'login.html')
#
# def register(request):
#     form = UserCreationForm()
#     context = {'form':form}
#     return render(request, 'register.html')

def single(request):
    products = Product.objects.all()
    return render(request, 'single.html', {'products': products})

def product(request, id):
    # product = Product.objects.get(id=id)
    product = Product.objects.filter(id=id)
    return render(request, 'product.html', {'product': product})

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
