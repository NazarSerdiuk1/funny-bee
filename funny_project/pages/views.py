from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from catalog.models import Product


def index_view(request):
    # Виводимо кілька хітів продажу з каталогу на головну сторінку
    hit_products = Product.objects.filter(is_hit=True)[:3]
    context = {
        'hit_products': hit_products,
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message_text = request.POST.get('message')
        
        if name and phone and message_text:
            ContactMessage.objects.create(
                name=name,
                phone=phone,
                message=message_text
            )
            
            return redirect('contacts')
            
    return render(request, 'contacts.html')