from django.contrib import admin
from.models import Review

class ReviewsAdmin(admin.ModelAdmin):
    list_display=("customer_name","comment","date","rating")

admin.site.register(Review,ReviewsAdmin)   
# Register your models here.
