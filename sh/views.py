from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from sh.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout

def show(request):
    products=product.objects.filter(trending=1)
    return render(request,'shop/shop.html',{"products":products})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfully")
    return redirect("/")

def login_page(request):
      if request.user.is_authenticated:
          return redirect("/")
      else:
        if request.method=="POST":
                uname=request.POST.get('username')
                pname=request.POST.get('password')
                user=authenticate(request,username=uname,password=pname)
                if user is not None:
                    login(request,user)
                    messages.error(request,"logged successfully")
                    return redirect("/")
                else:
                    messages.error(request,"Invalid user")
                    return redirect("/login")
        return render(request,'shop/login.html')
      

def cart_page(request):
  if request.user.is_authenticated:
    cart=Cart.objects.filter(user=request.user)
    return render(request,"shop/cart.html",{"cart":cart})
  else:
    return redirect("/")
 
def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")

  
def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registered successful")
            return redirect('/login')
    return render(request,'shop/register.html',{"form":form})


def collections(request):
    Category=category.objects.filter(status=0)
    return render(request,'shop/collections.html',{"Category":Category})
def collections_view(request,name):
    if(category.objects.filter( name=name,status=0)):
        products=product.objects.filter(category__name=name)
        return render(request,"shop/produvts/index.html",{"product":products,"Category_name":name})
    else:
        messages.warning(request,"NO such catagory found")
        return redirect('collections')
    
def product_details(request,cname,pname):
    if(category.objects.filter(name=cname,status=0)):
        if(product.objects.filter(name=pname,status=0)):
            products=product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/produvts/product_details.html",{"products":products})
        else:
            messages.error(request,"No such product found")
            return redirect("collections")
    else:
        messages.error(request,"no such category found")
        return redirect('collections')

    


# Create your views here.
