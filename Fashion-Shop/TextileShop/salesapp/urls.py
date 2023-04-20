from django.urls import path
from salesapp import views

urlpatterns = [
    path('sales_index/',views.indexSales, name='salesapp-indexSales'),
    path('sales/',views.sales, name='salesapp-sales'),
    path('sales/delete<int:pk>/',views.sales_delete, name='salesapp-sales-delete'),
    path('sales/update<int:pk>/',views.sales_update, name='salesapp-sales-update'),
    path('order/',views.order, name='salesapp-order'),
    path('logout/',views.logout, name='salesapp-logout'),
    path('report', views.pdf_report_create, name='salesapp-report'),
    #################
    path('adminpage',views.adminpage, name = "authentication-adminpage"),
    path('',views.index, name = "index"),
]