from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    name_category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name_category',)
class Product(models.Model):
    name_product = models.CharField(max_length=200, verbose_name='наименование')
    description = models.CharField(max_length=1000, verbose_name='описание')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'дата последнего изменения')

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name_product',)