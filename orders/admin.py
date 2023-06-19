from django.contrib import admin
from.models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_orders=("userId","products","totalPrics","shippingAddress","order_date")

admin.site.register(Orders, OrdersAdmin)


# Register your models here.
