from django.shortcuts import render, redirect
from .models import Cart
from .forms import CartUploadForm


def cart_upload(request):
    if request.method=="POST":
        form = CartUploadForm(request.POST)
        
        if form.is_valid():
            cart=form.save()
            cart.save()
    else:
        form=CartUploadForm()
    return render(request, "shoppingcart/cart_upload.html",{"form":form})            

    
def cart_products(request):
    cart= Cart.objects.all()
    return render (request, "shoppingcart/cart_list.html", {"cart":cart})


def edit_cart(request,id):
    cart= Cart.objects.all(id = id)
    
    if request.method=="POST":
         form= CartUploadForm(request.POST, instance=cart)
         if form.is_valid():
             form.save()
         return redirect("cart_detail_view", id=cart.id)    
     
    else:
        form = CartUploadForm(instance= cart)
        return render(request, "shoppingcart/ edit_cart.html", {"form":form})
 
        
         
# Create your views here.
