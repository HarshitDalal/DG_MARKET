from django.contrib import admin
from seller.models import SellerDetails,SellerReq

# Register your models here.
@admin.register(SellerDetails)
class SellerDetailsAdmin(admin.ModelAdmin):
    list_display=['Seller','Mobile_Number','Country','State','City','PinCode','ShopAddress']

@admin.register(SellerReq)
class SellerReqAdmin(admin.ModelAdmin):
    list_display=['Seller_Name','Email','Mobile','Product_Type']