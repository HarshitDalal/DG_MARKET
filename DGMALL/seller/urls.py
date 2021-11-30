from django.urls import path,include
from seller import views

urlpatterns = [
    path('',views.sell,name='sellerhome'),
    path('sellproduct/',views.sellProduct,name='sellproduct'),
    # path('sellrequest/login/',views.sellerLogin,name='sellerLogin'),
]