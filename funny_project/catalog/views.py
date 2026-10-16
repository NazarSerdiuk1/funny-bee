from django.shortcuts import render, get_object_or_404

from .models import Product, Category

def catalog_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    # Фільтрація за категорією (якщо передана в GET-параметрах)
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'catalog.html', context)

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)