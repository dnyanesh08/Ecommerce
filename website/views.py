from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from .forms import ProductForm
from django.http import JsonResponse
import json


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop.html', {'products': products})

def contact(request):
    return render(request, 'contact.html')

def product(request, id):
    # product = Product.objects.get(id=id)
    product = Product.objects.filter(id=id)
    return render(request, 'product.html', {'product': product})

# def shop(request):
#
#     products = Product.objects.all()
#     if request.user.is_authenticated:
#         # customer = request.user.customer
#         customer, created = Customer.objects.get_or_create(user=request.user)
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_item': 0}
#     context = {'items': items, 'order': order, 'products':products}
#     return render(request, 'shop.html', context)

def cart(request):

    if request.user.is_authenticated:
        # customer = request.user.customer
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}
    context = {'items': items, 'order': order}

    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)
    return JsonResponse('Item was added', safe=False)