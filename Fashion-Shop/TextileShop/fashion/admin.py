from django.contrib import admin
from fashion.models import Ordermngr,Supplier,Order,SupplierCancelDetails
# Register your models here.
class OrdermngrAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ordermngr, OrdermngrAdmin)

class SupplierAdmin(admin.ModelAdmin):
    pass
admin.site.register(Supplier, SupplierAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)

class SupplierCancelDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(SupplierCancelDetails, SupplierCancelDetailsAdmin)
