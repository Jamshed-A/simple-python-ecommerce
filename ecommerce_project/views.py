from django.http import HttpResponse
from django.shortcuts import render
from apps.products.models import Category, Product

def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)[:6]  # Get 6 popular products
    context = {
        'categories': categories,
        'products': products,
        'site_name': "JAY DEE'S",
        'tagline': "Your Style, Your Store"
    }
    return render(request, 'home.html', context)