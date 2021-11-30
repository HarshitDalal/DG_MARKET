from django.contrib import admin
from shop.models import ContactUs,UserDetails,ProductsDetails,Order
# Register your models here.

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['User','Firstname','Lastname','Profile_Pic','Email','Mobile','Address']

@admin.register(ProductsDetails)
class ProductsDetailsAdmin(admin.ModelAdmin):
    list_display = ['Seller','Product_Name','Cateogry','Price','Discount','Quantity','Main_Image','image_2','image_3','image_4','image_5']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile','decp']

admin.site.register(Order)