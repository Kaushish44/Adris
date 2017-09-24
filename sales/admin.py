from django.contrib import admin
from sales.models import customers, orders, menu

# Register your models here.
admin.site.register(customers)
admin.site.register(orders)
admin.site.register(menu)