from django.contrib import admin
from.models import SearchEngine

class SearchAdmin(admin.ModelAdmin):
    list_display=("userId","searchQuerry","results","timestamp")

admin.site.register(SearchEngine, SearchAdmin)    

# Register your models here.
