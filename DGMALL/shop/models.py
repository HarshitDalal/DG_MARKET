from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django_countries.fields import CountryField
from seller.models import SellerDetails

# # Create your models here.

class UserDetails(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE ,primary_key=True)
    Profile_Pic = models.ImageField(upload_to='User_Profile_pics')
    Firstname = models.CharField(max_length=70)
    Lastname = models.CharField(max_length=70)
    Email = models.EmailField(max_length=254)
    Mobile = models.CharField(max_length=20)
    Country = CountryField(default='INDIA')
    Address = models.TextField(blank=True)
    PinCode = models.CharField(max_length=10)
    Bio = models.TextField(blank=True)

    def __str__(self):
        return str(self.User)

class ProductsDetails(models.Model):
    product_type_choice ={
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
    }

    Seller = models.ForeignKey(SellerDetails,on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=150)
    Cateogry = models.CharField(max_length=50,choices=product_type_choice,default="Cloths")
    Price = models.CharField(max_length=20,blank=True)
    Discount = models.CharField(max_length=20,blank=True)
    Quantity = models.IntegerField(default=1)
    Color = models.CharField(max_length=10)
    Size = models.CharField(max_length=150)
    Small_Decription = models.TextField(blank=True,help_text='Describe product in 200 letters',max_length=200)
    Main_Image = models.ImageField(upload_to = 'product/images',default='none')
    image_2 = models.ImageField(upload_to = 'product/images',default='none')
    image_3 = models.ImageField(upload_to = 'product/images',default='none')
    image_4 = models.ImageField(upload_to = 'product/images',default='none')
    image_5 = models.ImageField(upload_to = 'product/images',default='none')
    Details = models.TextField(blank=True)
    Seller_Address = models.CharField(max_length=200)
    Seller_Email = models.EmailField(max_length=64)
    Seller_Mobile = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Seller)

    

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=64)
    mobile = models.CharField(max_length=20)
    decp = models.TextField(max_length=150)

class Order(models.Model):
    Buyer = models.CharField(max_length=150)
    Address = models.TextField(max_length=450)
    PinCode = models.CharField(max_length=7)
    Email = models.EmailField(max_length=150)   
    ProductName = models.CharField(max_length=150)
    ProductQty = models.CharField(max_length=150)
    ProductSize = models.CharField(max_length=150)
    ProductColor = models.CharField(max_length=150)
    ProductImg = models.URLField(max_length=150)
    ProductPrice = models.CharField(max_length=150)
    SellerEmail = models.EmailField(max_length=150)
    SellerName = models.CharField(max_length=150)
    SellerPhone = models.CharField(max_length=15,default='')
    Phone = models.CharField(max_length=15)

    def __str__(self):
        return self.Buyer
