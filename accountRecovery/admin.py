from django.contrib import admin
from.models import AccountRecovery

class AccountRecoveryAdmin(admin.ModelAdmin):
    list_display=("userId","email")

admin.site.register(AccountRecovery,AccountRecoveryAdmin)   
# Register your models here.
