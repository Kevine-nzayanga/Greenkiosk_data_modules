from django.contrib import admin
from.models import Refund

class RefundAdmin(admin.ModelAdmin):
    list_display = ("orderId","refundId","amount","reason","status","requestDate","processedDate")


admin.site.register(Refund,RefundAdmin)
# Register your models here.
