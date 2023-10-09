from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('product/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
]
