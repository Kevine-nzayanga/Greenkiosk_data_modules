from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from inventory.models import Product

    
def cart_products(request):
    cart= Cart.objects.all()
    return render (request, "shoppingcart/cart_list.html", {"cart":cart})
    
    
def product_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create()
    cart.products.add(product)
    cart.save()


def cart_view(request):
    cart = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})



def add_to_cart(request):
    # product = Product.objects.get(id=product_id)
    user_cart, created = Cart.objects.get_or_create()
    cart_products = user_cart.products.all()
    total_price = sum(product.price for product in cart_products)
    context = {
        'cart_products': cart_products,
        'total_price': total_price,
    }
    return redirect('cart/cart.html', context)


    


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
    cart_item.delete()
     
# Create your views here.
