from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
    return render(request, 'catalog/contact.html')