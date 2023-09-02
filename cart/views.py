from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from inventory.models import Product

    
def cart_products(request):
    cart= Cart.objects.all()
    return render (request, "shoppingcart/cart_list.html", {"cart":cart})
    


def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})



def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, item_created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not item_created:
        cart_item.product_qty += 1
        cart_item.save()
    
    return redirect('cart.html', product_id= product.id)

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
    cart_item.delete()
     
         
# Create your views here.
