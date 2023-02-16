from re import A
from django.contrib import admin
from .models import Categories
from .models import Products
from .models import Orders
from .models import Order_In_Wrork


admin.site.register(Orders)
admin.site.register(Products)
admin.site.register(Categories)

class OrdersAdmin(admin.ModelAdmin):
    list_display=["ord_name","phone_number","order_info"]
admin.site.register(Order_In_Wrork,OrdersAdmin)
# Register your models here.
