from django.urls import path
from store import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.order_detail, name='order_detail'),
    path('checkout/', views.checkout, name='checkout'),
     path('order-confirmation/', views.send_order_confirmation_email, name='order_confirmation'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
     path('done', views.done)
]
