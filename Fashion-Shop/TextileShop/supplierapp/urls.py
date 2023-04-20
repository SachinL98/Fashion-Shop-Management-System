from django.urls import path
from supplierapp import views

urlpatterns =[
    path('sales/',views.indexsup,name='supplierapp-index'),
    path('staff/',views.staff,name='supplierapp-staff'),
    path('supplier/',views.supplier,name='supplierapp-supplier'),
    path('supplier/delete/<int:pk>/',views.supplier_delete,name='supplierapp-supplier-delete'),
    path('supplier/update/<int:pk>/',views.supplier_update,name='supplierapp-supplier-update'),
    path('location/',views.location,name='supplierapp-location'),
    path('supplierReport/',views.supplierReport,name='supplierapp-SupplierReport'),
    #######################
    path('adminpage',views.adminpage, name = "authentication-adminpage"),
    path('',views.index, name = "index"),
]
