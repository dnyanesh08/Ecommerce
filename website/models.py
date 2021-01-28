from django.db import models
from django.contrib.auth.models import User, auth


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    base_price = models.IntegerField(null=True)
    ch_price = models.CharField(max_length=50)
    platename = models.CharField(max_length=100)
    offer = models.BooleanField(default=False)
    image = models.ImageField()
    desc = models.TextField()
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    digital = models.BooleanField(default=False, null=True,blank=False)
    # charector = models.ForeignKey(Charector, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    # @property
    # def your_price(self, **args):
    #     # total = (len(self.charector.name) - self.charector.name.count(" ")) * 20 + self.base_price
    #     # charector = self.charector_set.all()
    #     total = (len(self.charector.name) - self.charector.name.count(" ")) * 20 + self.base_price
    #     return total


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Charector(models.Model):
    name = models.CharField(max_length=100,  null=True, blank=True, unique=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    # total = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def your_price(self):
        total = (len(self.name) - self.name.count(" ")) * 20
        return total

    # @property
    # def your_price(self):
    #     total = (len(self.name) - self.name.count(" ")) * 20
    #     return total

    # @property
    # def base_price(self):
    #     return self.product.base_price


    # def total(self, product):
    #     # if self.product is None:
    #     #     return self.your_price
    #     total = self.your_price + product.base_price
    #     return f"{self.your_price} + {product.base_price} = {total}"
















# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=50, null=True)
#     email = models.CharField(max_length=50, null=True)
#
#     def __str__(self):
#         return self.user
#
#
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=False)
#     transaction_id = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return str(self.id)
#
#     @property
#     def shipping(self):
#         shipping = False
#         orderitems = self.orderitem_set.all()
#         for i in orderitems:
#             if i.product.digital == False:
#                 shipping = True
#
#         return shipping
#
#     @property
#     def get_cart_total(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.get_total for item in orderitems])
#         return total
#
#     @property
#     def get_cart_items(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.quantity for item in orderitems])
#         return total
#
# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     @property
#     def get_total(self):
#         total = self.product.price * self.quantity
#         return total
#
#     # def __str__(self):
#     #     return self.order
#
# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     address = models.CharField(max_length=200, null=True)
#     city = models.CharField(max_length=50, null=True)
#     state = models.CharField(max_length=50, null=True)
#     zipcode = models.CharField(max_length=50, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.address
#
