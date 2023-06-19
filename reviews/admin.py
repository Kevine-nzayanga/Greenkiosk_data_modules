from django.contrib import admin
from.models import Reviews

class ReviewsAdmin(admin.ModelAdmin):
    list_display=("customer_name","comment","date","rating")

admin.site.register(Reviews,ReviewsAdmin)   
# Register your models here.
