from django.contrib import admin
from.models import CartItem, Cart

class CartItemAdmin(admin.ModelAdmin):
    list_display=("product", "product_qty","price","discount")

admin.site.register(CartItem, CartItemAdmin)



class CartAdmin(admin.ModelAdmin):
    list_display=("name","get_products","timestamp")
    
    def get_products(self, cart):
        return cart.items.all()

admin.site.register(Cart, CartAdmin)



# Register your models here.
