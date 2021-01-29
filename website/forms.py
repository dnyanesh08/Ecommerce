from django import forms
from .models import Product
from .models import Charector


class CharectorForm(forms.ModelForm):

    class Meta:
        model = Charector
        fields = ('name',)




class ProductForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Product

        # specify fields to be used
        fields = "__all__"

