from django.urls import path,include
from shop import views
from seller import views as sell

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('product/',views.product,name='product'),
    path('product/productdetail/<int:myid>',views.productdetails,name='productdetail'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('registration/',views.registration,name='registration'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('profile/',views.profile,name='profile'),
    path('bucket/',views.bucket,name='bucket'),
    path('blog/',views.blog,name='blog'),
    path('order/',views.orderitem,name='order'),
    path('sellrequest/',sell.sellerLogin,name='sellerlogin'), 
]
