from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),
    path('<slug:slug>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('create/', views.BlogPostCreateView.as_view(), name='blog_post_create'),
    path('<slug:slug>/update/', views.BlogPostUpdateView.as_view(), name='blog_post_edit'),
    path('<slug:slug>/delete/', views.BlogPostDeleteView.as_view(), name='blog_post_delete'),

]
