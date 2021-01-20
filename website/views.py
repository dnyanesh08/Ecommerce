from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from .forms import ProductForm
from django.http import JsonResponse
import json
# import razorpay
from django.views.decorators.csrf import csrf_exempt
import datetime
from . utils import cookieCart, cartData

def index(request):
    products = Product.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'products': products, 'cartItems': cartItems}
    return render(request, 'index.html', context)



def contact(request):
    products = Product.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'products': products, 'cartItems': cartItems}
    return render(request, 'contact.html', context)

def product(request, id):
    # product = Product.objects.get(id=id)
    product = Product.objects.filter(id=id)

    charector = Charector.name
    # data = cartData(request)
    # cartItems = data['cartItems']
    # order = data['order']
    # items = data['items']
    price = {'total_price'}

    # final_price = price['total_price']

    # context = {'items': items, 'order': order,  'product': product, 'cartItems': cartItems, 'charector': charector}
    # return render(request, 'product.html', context)

    context = {'product': product,'charector': charector}
    # return HttpResponseRedirect("/product")
    return render(request, 'product.html', context)

def shop(request):
    products = Product.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'products': products, 'cartItems': cartItems}
    return render(request, 'shop.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}

    return render(request, 'cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    # customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        # customer = request.user.customer
        order, created = Order.objects.get_or_create(complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                # user=user,
                order=order,
                # firstname=data['shipping']['firstname'],
                # lastname=data['shipping']['lastname'],
                # mobile=data['shipping']['mobile'],
                # address1=data['shipping']['address1'],
                # address2=data['shipping']['address2'],
                # town=data['shipping']['town'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('User is not logged in..')
    return JsonResponse('Payment Complete!', safe=False)

def payment(request):
    return render(request, 'payment.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")


def count(request):
    product = Product.objects.filter(id=id)

    charector = Charector.name
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    price = {'total_price'}

    # final_price = price['total_price']

    context = {'items': items, 'product': product, 'charector': charector}
    return render(request, 'product.html', context)

