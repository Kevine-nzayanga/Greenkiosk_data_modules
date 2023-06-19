from django.contrib import admin
from.models import Discount

class DiscountAdmin(admin.ModelAdmin):
    list_display=("code","percentage","expiry_date")
    
admin.site.register(Discount,DiscountAdmin)    
# Register your models here.
