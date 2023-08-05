from django.shortcuts import render
from .models import Cart

def cart_products(request):
    cart= Cart.objects.all()
    return render (request, "shoppingcart/cart_list.html", {"cart":cart})
# Create your views here.
