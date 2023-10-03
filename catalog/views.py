from django.shortcuts import render
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'catalog/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
    return render(request, 'catalog/contact.html')


def product_detail(request, product_id):
    # Получаем информацию о товаре по его идентификатору
    product = Product.objects.get(pk=product_id)

    return render(request, 'catalog/product_detail.html', {'product': product})