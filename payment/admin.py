from django.contrib import admin
from.models import PaymentMethod

class PaymentAdmin(admin.ModelAdmin):
    list_display= ("userId","orderId","payment_method","payment_amount","transactionId")

admin.site.register(PaymentMethod,PaymentAdmin)
# Register your models here.
