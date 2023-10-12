from django.contrib import admin
from .models import Product, Category, Version

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_category')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version_number', 'version_name', 'is_active')