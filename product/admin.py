from django.contrib import admin
from.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","description","price","quantity","category")

admin.site.register(Product,ProductAdmin)


# Register your models here.
