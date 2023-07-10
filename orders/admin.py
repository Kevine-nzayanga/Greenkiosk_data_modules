from django.contrib import admin
from.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_orders=("payment","customer","products","totalPrice","shippingAddress","order_date","orderDate_update","cart")

admin.site.register(Order, OrderAdmin)


# Register your models here.
