from django.urls import path
from catalog.views import index, contact
from . import views

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]