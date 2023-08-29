from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart

# def update_total(request):
#     self.total = sum(ite)
    
@login_required   
def add_cart(request, product_id):
    cart=Cart(request)
    cart.add(product_id)
    
    return render(request, "shoppingcart/add_cart.html", {"form":cart})

    
def cart_products(request):
    cart= Cart.objects.all()
    return render (request, "shoppingcart/cart_list.html", {"cart":cart})
    

# def cart_upload(request):
#     if request.method=="POST":
#         form = CartUploadForm(request.POST)
        
#         if form.is_valid():
#             cart=form.save()
#             cart.save()
#     else:
#         form=CartUploadForm()
#     return render(request, "shoppingcart/cart_upload.html",{"form":form})            



# def edit_cart(request,id):
#     cart= Cart.objects.all(id = id)
    
#     if request.method=="POST":
#          form= CartUploadForm(request.POST, instance=cart)
#          if form.is_valid():
#              form.save()
#          return redirect("cart_detail_view", id=cart.id)    
     
#     else:
#         form = CartUploadForm(instance= cart)
#         return render(request, "shoppingcart/ edit_cart.html", {"form":form})
 
        
         
# Create your views here.
