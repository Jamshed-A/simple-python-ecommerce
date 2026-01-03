# Test script to verify the e-commerce application
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from apps.products.models import Category, Product
from django.contrib.auth.models import User

print("E-Commerce Application Verification:")
print("=====================================")

# Check if models exist
print(f"Categories in database: {Category.objects.count()}")
print(f"Products in database: {Product.objects.count()}")
print(f"Users in database: {User.objects.count()}")
print(f"Superusers in database: {User.objects.filter(is_superuser=True).count()}")

# Check sample categories
categories = Category.objects.all()
print(f"\nCategories:")
for cat in categories:
    print(f"  - {cat.name}: {cat.description}")

# Check sample products
products = Product.objects.all()
print(f"\nProducts:")
for prod in products:
    print(f"  - {prod.name} (${prod.price}): {prod.category}")

print(f"\nApplication is ready to run!")
print("Start the server with: python manage.py runserver 8000")
print("Visit: http://127.0.0.1:8000/")
print("Admin: http://127.0.0.1:8000/admin/ (admin/admin123)")