from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from .forms import ProductForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf \
import csrf_protect

import datetime
from .forms import CharectorForm
from django.contrib import messages
# from .forms import OrderForm
# from . utils import cookieCart, cartData

# def index(request):
#     products = Product.objects.all()
#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']
#
#     context = {'items': items, 'order': order, 'products': products, 'cartItems': cartItems}
#     return render(request, 'index.html', context)


def index(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'index.html', context)


def shop(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'shop.html', context)

def contact(request):

    return render(request, 'contact.html')


def product(request, id):
    product = Product.objects.filter(id=id)
    print(product)
    if request.method == "POST":
        form = CharectorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = CharectorForm()



    charectors = Charector.objects.all()
    # print(charectors)


    context = {'product': product, 'form': form, 'charectors': charectors,}
    return render(request, 'product.html', context)

@csrf_protect
def order(request):
    # products = Product.objects.all()


    amount = request.POST["amount"]
    name_on_plate = request.POST["name_on_plate"]
    frame = request.POST["frame"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    mobile = request.POST["mobile"]
    address = request.POST["address"]
    town = request.POST["town"]
    city = request.POST["city"]
    state = request.POST["state"]
    zip_code = request.POST["zip_code"]
    transaction_no = request.POST["transaction_no"]

    order_data = Order(amount=amount, name_on_plate=name_on_plate, frame=frame, first_name=first_name, last_name=last_name, email=email, mobile=mobile, address=address, town=town, city=city, state=state, zip_code=zip_code, transaction_no=transaction_no)
    order_data.save()


    messages.success(request, 'Your Order Placed Successfully...! Thanks For Order...!')
    return redirect("/")
    # messages.success("Your Order Placed Successfully....!")

    # context = {'products': products}
    # return render(request, 'index.html', context)




# def cart(request):
#     product = Product.objects.filter()
#     print(product)
#     form = CharectorForm()
#     charectors = Charector.objects.filter()
#     print(charectors)
#     context = {'product': product, 'form': form, 'charectors': charectors}
#     return render(request, 'cart.html', context)
#






# def cart(request):
#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']
#
#     context = {'items': items, 'order': order, 'cartItems': cartItems}
#
#     return render(request, 'cart.html', context)
#
#





# def product(request, id):
#     # product = Product.objects.get(id=id)
#     product = Product.objects.filter(id=id)
#
#     if request.method == "POST":
#         form = CharectorForm(request.POST)
#         # char = request.POST['name']
#         if form.is_valid():
#             post = form.save(commit=False)
#             # total = (len(product.charector.name) - product.charector.name.count(" ")) * 20 + product.base_price
#             # total = {'your_price'}
#             post.save()
#             # return redirect('/', pk=post.pk)
#     else:
#         form = CharectorForm()
#
#     context = {'product': product, 'form': form}
#     return render(request, 'product.html', context)


    # data = cartData(request)
    # cartItems = data['cartItems']
    # order = data['order']
    # items = data['items']

    # final_price = price['total_price']

    # context = {'items': items, 'order': order,  'product': product, 'cartItems': cartItems, 'charector': charector}
    # return render(request, 'product.html', context)



























# def shop(request):
#     products = Product.objects.all()
#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']
#
#     context = {'items': items, 'order': order, 'products': products, 'cartItems': cartItems}
#     return render(request, 'shop.html', context)

# def cart(request):
#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']
#
#     context = {'items': items, 'order': order, 'cartItems': cartItems}
#
#     return render(request, 'cart.html', context)
#

# def checkout(request):
#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']
#
#     context = {'items': items, 'order': order, 'cartItems': cartItems}
#     return render(request, 'checkout.html', context)

# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#
#     print('Action:', action)
#     print('productId:', productId)
#
#     # customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(complete=False)
#
#     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#
#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)
#
#     orderItem.save()
#
#     if orderItem.quantity <= 0:
#         orderItem.delete()
#
#     return JsonResponse('Item was added', safe=False)

# def processOrder(request):
#     transaction_id = datetime.datetime.now().timestamp()
#     data = json.loads(request.body)
#     if request.user.is_authenticated:
#         # customer = request.user.customer
#         order, created = Order.objects.get_or_create(complete=False)
#         total = float(data['form']['total'])
#         order.transaction_id = transaction_id
#
#         if total == float(order.get_cart_total):
#             order.complete = True
#         order.save()
#
#         if order.shipping == True:
#             ShippingAddress.objects.create(
#                 # user=user,
#                 order=order,
#                 # firstname=data['shipping']['firstname'],
#                 # lastname=data['shipping']['lastname'],
#                 # mobile=data['shipping']['mobile'],
#                 # address1=data['shipping']['address1'],
#                 # address2=data['shipping']['address2'],
#                 # town=data['shipping']['town'],
#                 city=data['shipping']['city'],
#                 state=data['shipping']['state'],
#                 zipcode=data['shipping']['zipcode'],
#             )
#     else:
#         print('User is not logged in..')
#     return JsonResponse('Payment Complete!', safe=False)
#
# def payment(request):
#     return render(request, 'payment.html')
#
# @csrf_exempt
# def success(request):
#     return render(request, "success.html")

#
# def charector(request):
#     pass

