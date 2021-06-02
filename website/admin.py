from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Charector)
admin.site.register(Product)
admin.site.register(Order)


# admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(ShippingAddress)


admin.site.site_header = "ECommerce Admin Panel"

