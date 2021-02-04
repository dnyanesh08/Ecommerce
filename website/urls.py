from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('product/<id>', views.product, name='product'),
    path('shop.html', views.shop, name='shop'),


    # path('checkout.html', views.checkout, name='checkout'),
    # path('cart.html/', views.cart, name='cart'),
    # path('update_item/', views.updateItem, name='update_item'),
    # path('charector/', views.charector, name='charector'),
    # path('payment.html/', views.payment, name='payment'),
    # path('process_order/', views.processOrder, name='process_order'),
    # path('success', views.success, name='success')

]