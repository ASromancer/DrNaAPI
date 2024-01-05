from django.contrib import admin
from .models import Consumables, Customers, OrderDetails, Orders, Services

# Register your models with the admin site
admin.site.register(Consumables)
admin.site.register(Customers)
admin.site.register(OrderDetails)
admin.site.register(Orders)
admin.site.register(Services)
