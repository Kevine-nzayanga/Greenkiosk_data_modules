from django.contrib import admin
from.models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ("product_name","product_id","price","discount")

admin.site.register(Cart,CartAdmin)    

# Register your models here.
