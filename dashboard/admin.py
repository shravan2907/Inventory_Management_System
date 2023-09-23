from django.contrib import admin
from .models import Product, Transactions
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'WelInventory Admin Page'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity')
    list_filter = ['category']

admin.site.register(Product,ProductAdmin)
admin.site.register(Transactions)
# admin.site.unregister(Group)