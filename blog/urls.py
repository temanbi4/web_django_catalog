from django.urls import path
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blogpost_list'),
    path('blog/<str:slug>', BlogDetailView.as_view(), name='blogpost_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blogpost_create'),
    path('blog/edit/<str:slug>', BlogUpdateView.as_view(), name='blogpost_edit'),
    path('blog/delete/<str:slug>', BlogDeleteView.as_view(), name='blogpost_delete'),
]