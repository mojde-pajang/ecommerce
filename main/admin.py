from django.contrib import admin
from django.contrib.auth.models import Group
from main.models import Customer, Order, Product

# Register your models here.
admin.site.unregister(Group)
@admin.register(Customer, Order, Product)
class PersonAdmin(admin.ModelAdmin):
    pass