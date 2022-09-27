from django.contrib import admin
from . models import Store


# Register your models here.
# admin.site.register(Store)

@admin.register(Store)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('product','price','quantity')
    search_fields = ('product','price')
    list_filter = ('quantity',)










