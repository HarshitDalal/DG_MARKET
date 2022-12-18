from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class SellerDetails(models.Model):
    Profile_Pic = models.ImageField(
        upload_to='Seller_Profile_Pics', default=None)
    Seller = models.OneToOneField(User, limit_choices_to={
                                  'is_staff': True}, on_delete=models.CASCADE, primary_key=True)
    Email = models.EmailField(max_length=84, default="")
    Mobile_Number = models.CharField(max_length=20)
    Country = CountryField(default='INDIA')
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    PinCode = models.CharField(max_length=10)
    ShopAddress = models.CharField(max_length=250)

    def __str__(self):
        return str(self.Seller)


product_type_choice = [
    ('Accessories', 'Accessories'),
    ('Appliances', 'Appliances'),
    ('Cloths', 'Cloths'),
    ('Cosmetic', 'Cosmetic'),
    ('Electronics', 'Electronics'),
    ('Fashions', 'Fashions'),
    ('Fitness', 'Fitness'),
    ('Grocery', 'Grocery'),
    ('HomeDecoretion', 'HomeDecoretion'),
    ('OfficeFuniture', 'OfficeFuniture'),
    ('Sports', 'Sports'),
    ('Toys', 'Toys'),
]

class SellerReq(models.Model):
    Seller_Name = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    Email = models.EmailField(max_length=84, default="")
    Mobile = models.CharField(max_length=50)
    Massage = models.TextField(max_length=200)
    Product_Type = models.CharField(
        max_length=20, choices=product_type_choice, default='Cloths')

    def __str__(self):
        return str(self.Seller_Name)