from django.contrib import admin
from .models import Shipment

class ShipmentAdmin(admin.ModelAdmin):
    list_shipment = ("orders","tracking_number","destination","date_shpped")
    
  
admin.site.register(Shipment, ShipmentAdmin)

# Register your models here.
