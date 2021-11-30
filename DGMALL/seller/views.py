from django.shortcuts import redirect, render
from shop.models import ProductsDetails
from django.contrib.admin.views.decorators import staff_member_required
from seller.forms import SellRequest,SellerForm,ProductForm
from seller.models import SellerDetails,SellerReq
from django.core.mail import send_mail,send_mass_mail
from django.contrib import messages
from DGMALL.settings import EMAIL_HOST_USER

# Create your views here.
@staff_member_required(login_url='/sellrequest/')
def sell(request):
    try:
        seller = request.user.sellerdetails
        if seller:
            sfm = SellerForm(instance=seller)
            if request.method == 'POST':
                sfm = SellerForm(request.POST,request.FILES,instance=seller)
                if sfm.is_valid():
                    sfm.save()
                    messages.success(request,f"{request.user} Your Details Successfully Update.")
                else:
                    messages.error(request,"Details Not Update.")
        else:
            sfm = SellerForm()
    except Exception as e:
        if request.method == 'POST':
            sfm = SellerForm(request.POST,request.FILES)
            if sfm.is_valid():
                sfm.save()
                messages.success(request,f"{request.user} Your Seller Account Successfully Created.")
            else:
                messages.error(request,"Fill All Fields Carefully Again.")
        else:
            sfm = SellerForm()
    return render(request,'base.html',{'sfm':sfm})

@staff_member_required
def sellProduct(request):
    if request.method == "POST" :
        fm = ProductForm(request.POST)
        if fm.is_valid():
            Seller = fm.cleaned_data['Seller']
        Product_Name = request.POST['product_name']
        Cateogry = request.POST['Cateogry']
        Price = request.POST['real_price']
        Discount = request.POST['discount_price']
        Quantity = request.POST['quantity']
        Size = request.POST['size']
        Color = request.POST['color']
        Small_Decription = request.POST['small_description']
        Main_Image = request.FILES['file1']
        image_2 = request.FILES['file2']
        image_3 = request.FILES.get('file3',None)
        image_4 = request.FILES.get('file4',None)
        image_5 = request.FILES.get('file5',None)
        Details = request.POST['long_description']
        Seller_Email = request.POST['email']
        Seller_Mobile = request.POST['phone']
        Seller_Address = request.POST['shop_address']
        productFill = ProductsDetails(
            Product_Name=Product_Name,
            Cateogry=Cateogry,
            Price=Price,
            Discount=Discount,
            Quantity=Quantity,
            Size = Size,
            Color = Color,
            Small_Decription=Small_Decription,
            Main_Image=Main_Image,
            image_2=image_2,
            image_3=image_3,
            image_4=image_4,
            image_5=image_5,
            Details=Details,
            Seller=Seller,
            Seller_Email = Seller_Email,
            Seller_Mobile = Seller_Mobile,
            Seller_Address = Seller_Address
        )
        try:
            productFill.save()
            messages.success(request,'Product Added Succesefuly')
        except Exception as e:
            messages.error(request,"Some error occure! Fill allfield")
    else:
        fm = ProductForm()
    return render(request,'seller/sellproduct.html',{'fm':fm})
            
        


def sellerLogin(request):
    # Seller_D = request.user.SellerDetails
    if request.method == "POST":
        sellerfm = SellRequest(request.POST)
        if sellerfm.is_valid():
            seller = sellerfm.cleaned_data['Seller_Name']
            email = sellerfm.cleaned_data['Email']
            mobile = sellerfm.cleaned_data['Mobile']
            message = sellerfm.cleaned_data['Massage']
            ptype = sellerfm.cleaned_data['Product_Type']
            sellerfmsv = SellerReq(Seller_Name=seller,Email=email,Mobile=mobile,Massage=message,Product_Type=ptype)
            msg1 = (
                'We Went To Sell Product',
                f'Hi I am {seller} .\n\n\t {message} .\n\n\t my Email id is {email} and contact number is {mobile}  \n\n\n My Product Type is {ptype} \n\n\t\t Thank You....',
                email,
                [EMAIL_HOST_USER]
            )
            msg2 = (
                'Request Recived',
                f'Hello Mr./Mrs. -{seller} .\n\n We recived your request send your Aadhar photo for id proof. Then we approve Your Request.. \n\n\n\t\t\t\t DG-Market\n\n\n\t\t\t\t {EMAIL_HOST_USER}',
                EMAIL_HOST_USER,
                [email]
            )
            done = send_mass_mail(
                (msg1,msg2),
                fail_silently=True
            )
            if done :
                messages.success(request,'Message Succesefuly Send')
                sellerfmsv.save()
                request.user.is_staff = True
                SellerDetails.objects.create(
                    Seller = request.user,
                )
                return redirect('/')
            else:
                messages.error(request,"Message Could Not Check Your Email Id")
    else:
        sellerfm = SellRequest()
    return render(request,'seller/sellerlogin.html',{'sellerfm':sellerfm})
