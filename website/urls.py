from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('product/<id>', views.product, name='product'),
    path('shop.html', views.shop, name='shop'),
    path('checkout.html', views.checkout, name='checkout'),
    path('cart.html/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update_item'),
    path('payment.html/', views.payment, name='payment')
    # path('men.html', views.men, name='men'),
    # path('kids.html', views.kids, name='kids'),
    # path('dailyneeds.html', views.dailyneeds, name='dailyneeds'),
    # path('organicfood.html', views.organicfood, name='organicfood'),
    # path('gifts.html', views.gifts, name='gifts'),
    # path('homedecor.html', views.homedecor, name='homedecor'),
    # path('furnitures.html', views.furnitures, name='furnitures')
]