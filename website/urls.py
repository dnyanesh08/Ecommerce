from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('products.html', views.products, name='products'),
    path('contact.html', views.contact, name='contact'),
    # path('login.html', views.login, name='login'),
    # path('register.html', views.register, name='register'),
    path('single.html', views.single, name='single'),
    path('product/<id>', views.product, name='product'),
    path('shop.html', views.shop, name='shop'),
    # path('men.html', views.men, name='men'),
    # path('kids.html', views.kids, name='kids'),
    # path('dailyneeds.html', views.dailyneeds, name='dailyneeds'),
    # path('organicfood.html', views.organicfood, name='organicfood'),
    # path('gifts.html', views.gifts, name='gifts'),
    # path('homedecor.html', views.homedecor, name='homedecor'),
    # path('furnitures.html', views.furnitures, name='furnitures')
]