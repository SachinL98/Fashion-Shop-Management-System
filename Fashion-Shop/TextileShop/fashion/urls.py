
from django.contrib import admin
from django.urls import path
from fashion import views
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('order/',views.home_view,name=''),
    
    # path('logout', LogoutView.as_view(template_name='fashion/index.html'),name='logout'),

    path('admin-dashboard/', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-ordermngr/', views.admin_ordermngr_view,name='admin-ordermngr'),
    path('admin-view-ordermngr/', views.admin_view_ordermngr_view,name='admin-view-ordermngr'),
    path('delete-ordermngr-from-fashion/<int:pk>', views.delete_ordermngr_from_fashion_view,name='delete-ordermngr-from-fashion'),
    path('update-ordermngr/<int:pk>', views.update_ordermngr_view,name='update-ordermngr'),
    path('admin-add-ordermngr/', views.admin_add_ordermngr_view,name='admin-add-ordermngr'),
    path('admin-approve-ordermngr/', views.admin_approve_ordermngr_view,name='admin-approve-ordermngr'),
    path('approve-ordermngr/<int:pk>', views.approve_ordermngr_view,name='approve-ordermngr'),
    path('reject-ordermngr/<int:pk>', views.reject_ordermngr_view,name='reject-ordermngr'),
    path('admin-view-ordermngr-specialisation/',views.admin_view_ordermngr_specialisation_view,name='admin-view-ordermngr-specialisation'),

    path('admin-supplier/', views.admin_supplier_view,name='admin-supplier'),
    path('admin-view-supplier/', views.admin_view_supplier_view,name='admin-view-supplier'),
    path('delete-supplier-from-fashion/<int:pk>', views.delete_supplier_from_fashion_view,name='delete-supplier-from-fashion'),
    path('update-supplier/<int:pk>', views.update_supplier_view,name='update-supplier'),
    path('admin-add-supplier/', views.admin_add_supplier_view,name='admin-add-supplier'),

    path('approve-supplier/<int:pk>', views.approve_supplier_view,name='approve-supplier'),
    path('reject-supplier/<int:pk>', views.reject_supplier_view,name='reject-supplier'),
    path('admin-cancel-supplier/', views.admin_cancel_supplier_view,name='admin-cancel-supplier'),
    path('cancel-supplier/<int:pk>', views.cancel_supplier_view,name='cancel-supplier'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),
    
    path('admin-view-cancel-supplier/', views.admin_view_cancel_supplier_view,name='admin-view-cancel-supplier'),
    path('admin-order/', views.admin_order_view,name='admin-order'),
    path('admin-view-order/', views.admin_view_order_view,name='admin-view-order'),
    path('admin-add-order/', views.admin_add_order_view,name='admin-add-order'),
    path('admin-approve-order/', views.admin_approve_order_view,name='admin-approve-order'),
    path('approve-order/<int:pk>', views.approve_order_view,name='approve-order'),
    path('reject-order/<int:pk>', views.reject_order_view,name='reject-order'),
    
    path('admin-view-cancel-supplier/printFile/', views.printFile,name='printFile'),
]



