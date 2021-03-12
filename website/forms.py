from django import forms
from .models import Product
from .models import Charector
from .models import Order

class CharectorForm(forms.ModelForm):

    class Meta:
        model = Charector
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'post-text',
                'required': True,
                'onclick': "this.value=''",
                'placeholder': 'Enter Your Name On Plate....',
                'class': 'char-input'
            }),
        }




class ProductForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Product

        # specify fields to be used
        fields = "__all__"


# class OrderForm(forms.ModelForm):
#
#     class Meta:
#         model = Order
#
#         fields = "__all__"
