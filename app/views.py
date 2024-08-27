from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages

# Making filter
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles, 'laptops':laptops }) #here the key is not necessaary to be same in dictionary but we write so that we not have any problem and here the values in dictionary are same the one we declare in the above lines
    
    

# def product_detail(request):
#     return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product = (Product.objects.get(pk=pk))
        return render(request, 'app/productdetail.html', {'product':product})
    

def add_to_cart(request):
    return render(request, 'app/addtocart.html')

def buy_now(request):
    return render(request, 'app/buynow.html')

def profile(request):
    return render(request, 'app/profile.html')

def address(request):
    return render(request, 'app/address.html')

def orders(request):
    return render(request, 'app/orders.html')

def change_password(request):
    return render(request, 'app/changepassword.html')

def mobile(request, data=None):   #int this line data=None is by default
    if data == None:   #And here it will check for data
        mobiles = Product.objects.filter(category='M')
    elif data == 'Redmi' or data == 'Samsung' or data == 'Apple':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles':mobiles})


def laptop(request, data=None):   #int this line data=None is by default
    if data == None:   #And here it will check for data
        laptops = Product.objects.filter(category='L')
    elif data == 'Dell' or data == 'Vivo' or data == 'Apple' or data == 'Lenovo':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(category='L').filter(discounted_price__lt=15000)
    elif data == 'above':
        laptops = Product.objects.filter(category='L').filter(discounted_price__gt=15000)
    return render(request, 'app/laptop.html', {'laptops':laptops})


def topwear(request, data=None):   #int this line data=None is by default
    if data == None:   #And here it will check for data
        topwears = Product.objects.filter(category='TW')
    elif data == 'Park' or data == 'Polo':
        topwears = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'below':
        topwears = Product.objects.filter(category='TW').filter(discounted_price__lt=450)
    elif data == 'above':
        topwears = Product.objects.filter(category='TW').filter(discounted_price__gt=450)
    return render(request, 'app/topwear.html', {'topwears':topwears})


def bottomwear(request, data=None):   #int this line data=None is by default
    if data == None:   #And here it will check for data
        bottomwears = Product.objects.filter(category='BW')
    elif data == 'Lee' or data == 'Spykar':
        bottomwears = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'below':
        bottomwears = Product.objects.filter(category='BW').filter(discounted_price__lt=500)
    elif data == 'above':
        bottomwears = Product.objects.filter(category='BW').filter(discounted_price__gt=500)
    return render(request, 'app/bottomwear.html', {'bottomwears':bottomwears})


# def login(request):
#     return render(request, 'app/login.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})


def checkout(request):
    return render(request, 'app/checkout.html')
