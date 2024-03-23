from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('view_review/<int:product_id>/', views.view_review, name='view_review'),
    path('edit_review/<int:product_id>/review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('delete_review/<int:product_id>/review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('subscription/', views.subscription, name='subscription'),
]
