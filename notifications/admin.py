from django.contrib import admin
from.models import Notifications

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ("userId","message","timestamp")

admin.site.register(Notifications,NotificationsAdmin)    
# Register your models here.
