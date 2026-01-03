from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)

    # Map category name to display name
    category_mapping = {
        'makeup': 'Makeup',
        'ladies_shoes': 'Ladies Shoes',
        'gents_shoes': 'Gents Shoes',
        'ladies_dresses': 'Ladies Dresses',
        'gents_dresses': 'Gents Dresses',
        'accessories': 'Accessories',
    }

    display_name = category_mapping.get(category.name, category.name)

    products = Product.objects.filter(category=category.name, available=True)
    return render(request, 'products/category_detail.html', {
        'category': category,
        'display_name': display_name,
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:4]
    return render(request, 'products/product_detail.html', {
        'product': product,
        'related_products': related_products
    })