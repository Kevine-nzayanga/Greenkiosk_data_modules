from django.contrib import admin
from.models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ("name","email","phoneNumber","address")
    
admin.site.register(Vendor,VendorAdmin)      

# Register your models here.
