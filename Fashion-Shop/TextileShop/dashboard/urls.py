from django.urls import path,include
from dashboard import views

urlpatterns =[
    path('finance_index/',views.indexSVD,name='dashboard-indexSVD'),
    path('employee/',views.employeeSVD,name='dashboard-employeeSVD'),
    path('employee/delete/<int:pk>',views.employee_deleteF,name='dashboard-employee_deleteF'),
    path('employee/update/<int:pk>',views.employee_updateF,name='dashboard-employee_updateF'),
    path('item/',views.itemSVD,name='dashboard-itemSVD'),
    path('order/',views.orderSVD,name='dashboard-orderSVD'),
    path('sales/',views.salesSVD,name='dashboard-salesSVD'),
    path('utility/',views.utilitySVD,name='dashboard-utilitySVD'),
    path('utility/delete/<int:pk>',views.utility_deleteF,name='dashboard-utility_deleteF'),
    path('utility/update/<int:pk>',views.utility_updateF,name='dashboard-utility_updateF'),
    path('report/',views.reportSVD,name='dashboard-reportSVD'),
    path('report_pdf/',views.reportSVD_pdf,name='dashboard-reportSVD_pdf'),
    path('search_result/',views.search_emp,name='dashboard-search_emp'),
    #######################
    path('adminpage',views.adminpage, name = "authentication-adminpage"),
    path('',views.index, name = "index"),
]