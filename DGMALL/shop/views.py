from django.shortcuts import render,redirect,HttpResponseRedirect
from shop.models import ContactUs, Order,ProductsDetails, UserDetails
from shop.forms import ContactForm ,RegistrationForm, UserDetailsForm, AdminProfileForm
from django.core.mail import send_mail,send_mass_mail
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login ,logout ,update_session_auth_hash


# Create your views here.

# home page
def home(request):
    allProds = ProductsDetails.objects.all().order_by('-pk')[:8]
    parms = {'newproducts': allProds}
    return render(request,'shop/home.html',parms)

# about page
def about(request):
    return render(request,'shop/about.html')

# product page 
def product(request):
    allProds = []
    catProds = ProductsDetails.objects.values('Cateogry','id')
    cats = {item['Cateogry'] for item in catProds}
    for cat in cats:
        prod = ProductsDetails.objects.filter(Cateogry=cat)
        n = len(prod)
        allProds.append([prod,range(1,n)])

    parms = {'products': allProds}
    return render(request,'shop/product.html',parms)

# productdetail page 
def productdetails(request, myid):
    product = ProductsDetails.objects.filter(id=myid)
    return render(request,'shop/productdetail.html',{'product':product[0]})

# logout page 
def logoutUser(request):
    logout(request)
    messages.success(request,'Logout Successfully.')
    return redirect('/login/')

# login page 
def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            logfm = AuthenticationForm(request=request, data=request.POST)
            if logfm.is_valid():
                uname = logfm.cleaned_data['username']
                upass = logfm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfully Done.')
                    return redirect('/profile/')
                else:
                    messages.error(request,'Password Or Username Not Match')
        else:
            logfm = AuthenticationForm()
        return render(request,'shop/login.html',{'logfm':logfm})
    else:
        return redirect('/profile/')

# registration page 
def registration(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            regfm = RegistrationForm(request.POST)
            if regfm.is_valid():
                user = regfm.save()
                UserDetails.objects.create(
                    User = user,
                    Email = user.email,
                )
                messages.success(request,'Registrations Successfully Done.')
                return redirect('/login/')
            else:
                messages.error(request,'Password Could Not Be Same As Email Or Username')
        else:
            regfm = RegistrationForm()
        return render(request,'shop/registration.html',{'regfm':regfm})
    else:
        return redirect('/profile/')

# changepassword page 
@login_required(login_url='/login/')
def changepassword(request):
    if request.method == "POST":
        chpass = PasswordChangeForm(user=request.user,data=request.POST)
        if chpass.is_valid():
            chpass.save()
            messages.success(request,'Password Has Been Changed')
            update_session_auth_hash(request,chpass.user)
            return redirect('/profile/')
        else:
            messages.error(request,'Password Not Change')
    else:
        chpass = PasswordChangeForm(user=request.user)
    return render(request,'shop/changepassword.html',{'chpass':chpass})

# forgotpassword page 
def forgotpassword(request):
    if request.method == "POST":
        fgpass = SetPasswordForm(user=request.user,data=request.POST)
        if fgpass.is_valid():
            fgpass.save()
            messages.success(request,'Password Has Been Changed')
            update_session_auth_hash(request,fgpass.user)
            return redirect('/profile/')
        else:
            messages.error(request,'Password Not Change')
    else:
        fgpass = SetPasswordForm(user=request.user)
    return render(request,'shop/forgotpassword.html',{'fgpass':fgpass})
        
# contact form page
def contact(request):
    if request.method == 'POST':      
        confm = ContactForm(request.POST)
        if confm.is_valid():
            name = confm.cleaned_data['name']
            email = confm.cleaned_data['email']
            mobile = confm.cleaned_data['mobile']
            decp = confm.cleaned_data['decp']
            contacts = ContactUs(name=name,email=email,mobile=mobile,decp=decp)
            send_mail(
                "Contact with me "+name,
                f"Hi -{name}\n\n\nThank you for give your feedback.\n\n \t We will contact as soon as possible on your email address - {email} or mobile number - +91{mobile}",
                'harshitdalal21@gmail.com',
                [email],
                fail_silently=True
            )
            contacts.save()
            messages.success(request,'Message Sended To DG MARKET.')
        else:
            messages.error(request,'Email Address Not Correct')     
        return render(request,'shop/contact.html',{'name':name})
    else:
        confm = ContactForm()
        return render(request,'shop/contact.html',{'confm':confm})

# profile page
@login_required(login_url='/login/')
def profile(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            fm = AdminProfileForm(request.POST,request.FILES,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,f'{request.user} Profile Successfully Update')
        else:
            fm = AdminProfileForm(instance=request.user)
    else:
        if request.method == "POST":
            fm = UserDetailsForm(request.POST,request.FILES,instance=request.user.userdetails)
            if fm.is_valid():
                fm.save()
                messages.success(request,f'{request.user} Profile Successfully Update')
        else:
            fm = UserDetailsForm(instance=request.user.userdetails)
    return render(request,'shop/profile.html',{'fm':fm})
   
#add to cart page
@login_required(login_url='/login/')
def bucket(request):
    return render(request,'shop/bucket.html')

#blog page
def blog(request):
    return render(request,'shop/blog.html')

#order item by customer page
@login_required(login_url='/login/')
def orderitem(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            img = request.POST['img']
            qty = request.POST['qty']
            size = request.POST['size']
            price = request.POST['subtotal']
            color = request.POST['color']
            seller = request.POST['seller']
            selleremail = request.POST['selleremail']
            sellerphone = request.POST['sellerphone']
            useremail = request.POST['useremail']
            buyer = request.POST['user']
            orders = Order(
                Buyer = buyer,
                Email = useremail,
                Address = request.user.userdetails.Address,
                PinCode = request.user.userdetails.PinCode,
                Phone = request.user.userdetails.Mobile,
                ProductImg = img,
                ProductName= name,
                ProductQty = qty,
                ProductSize = size,
                ProductColor = color,
                ProductPrice = price,
                SellerName = seller,
                SellerEmail = selleremail,
                SellerPhone = sellerphone,
            )
            orders.save()
            msg1 = (
                'You Got An Order',
                f'Form {buyer} \n\n\t deliver the product on this adddress {request.user.userdetails.Address} \n\t orderitem is {name} quantity -{qty} price -{price} color - {color} size - {size} img -{img} \n\n\n Buyers details \n buyer - {buyer}\n phone -{request.user.userdetails.Mobile}\n pincode -{request.user.userdetails.PinCode}',
                "dgmarket11@gmail.com",
                [selleremail]
            )
            msg2 = (
                'Order Placed',
                f'By {buyer} \n\n\t Your address - {request.user.userdetails.Address} \n\t orderitem is {name} quantity -{qty} price -{price} color - {color} size - {size} img -{img} \n\n\n Buyers details \n buyer - {buyer}\n phone -{request.user.userdetails.Mobile}\n pincode -{request.user.userdetails.PinCode} \n\n Seller details \n seller -{seller},contact -phone -{sellerphone}, email -{selleremail}',
                "dgmarket11@gmail.com",
                [useremail]
            )
            done = send_mass_mail(
                (msg1,msg2),
                fail_silently=True
            )
            messages.success(request,'Order Successfully Added Call Seller For Payment Method')

            orders = Order.objects.filter(Buyer=request.user.userdetails.User)
            print(orders)
            return render(request,'shop/order.html',{'orders':orders})

        else:
            orders = Order.objects.filter(Buyer=request.user.userdetails.User)
            print(orders)
            return render(request,'shop/order.html',{'orders':orders})
    except Exception as e:
        messages.error(request,e)
        return redirect('/profile/')

    