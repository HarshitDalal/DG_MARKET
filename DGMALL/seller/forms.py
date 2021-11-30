# from typing_extensions import Required
from django import forms
from django.db import models
from django.db.models.fields import TextField
from django.forms import fields, widgets
from seller.models import SellerDetails,SellerReq
from django_countries.widgets import CountrySelectWidget
from shop.models import ProductsDetails

class SellerForm(forms.ModelForm):
    class Meta:
        model = SellerDetails
        fields = '__all__'
        widgets = {
            'Country': CountrySelectWidget(),
        }
        exclude = ['user']

product_type_choice =[
    ('Accessories','Accessories'),
    ('Appliances','Appliances'),
    ('Cloths','Cloths'),
    ('Cosmetic','Cosmetic'),
    ('Electronics','Electronics'),
    ('Fashions','Fashions'),
    ('Fitness','Fitness'),
    ('Grocery','Grocery'),
    ('HomeDecoretion','HomeDecoretion'),
    ('OfficeFuniture','OfficeFuniture'),
    ('Sports','Sports'),
    ('Toys','Toys'),
]

class SellRequest(forms.ModelForm):
    class Meta:
        model = SellerReq
        fields = '__all__'
        exclude = ['user']

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductsDetails
        fields = ('Seller',)
        exclude = ['sellerdetails']