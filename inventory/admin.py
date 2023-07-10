from django.contrib import admin
from.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=("vendor","name","stock","price","date_created","date_updated")

admin.site.register(Product, ProductAdmin)

# Register your models here.
