from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):


    def handle(self, *args, **options):
        # Создаем категории
        category1 = Category.objects.create(name_category='Категория 1', description='Описание категории 1')
        category2 = Category.objects.create(name_category='Категория 2', description='Описание категории 2')

        # Создаем продукты
        product1 = Product.objects.create(
            name_product='Продукт 1',
            description='Описание продукта 1',
            category=category1,
            price=100.00
        )

        product2 = Product.objects.create(
            name_product='Продукт 2',
            description='Описание продукта 2',
            category=category2,
            price=150.00
        )

        self.stdout.write(self.style.SUCCESS('Данные успешно заполнены'))
