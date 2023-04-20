from django.urls import path
from stockapp import views

urlpatterns = [
    path('stock/', views.indexstock, name='stockapp-index'),
    path('item/', views.item, name='stockapp-item'),
    path('item/delete/<int:pk>/', views.item_delete, name='stockapp-item-delete'),
    path('item/update/<int:pk>/', views.item_update, name='stockapp-item-update'),
    path('report/', views.report, name='stockapp-report'),
    #######################
    path('adminpage',views.adminpage, name = "authentication-adminpage"),
    path('',views.index, name = "index"),
]