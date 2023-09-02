from django.contrib import admin
from.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name","date_of_birth", "email","phone_number","password")

admin.site.register(Customer, CustomerAdmin)

# Register your models here.
