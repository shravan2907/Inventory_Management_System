from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>', views.staff_detail, name='dashboard-staff-detail'),
    path('products/', views.products, name='dashboard-products'),
    path('products/delete/<int:pk>/', views.products_delete, name='dashboard-products-delete'),
    path('products/update/<int:pk>/', views.products_update, name='dashboard-products-update'),
    path('transactions/', views.transactions, name='dashboard-transactions')
]

