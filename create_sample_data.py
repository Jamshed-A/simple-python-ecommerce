from django.core.management import execute_from_command_line
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from apps.products.models import Category, Product
from django.contrib.auth.models import User

def create_sample_data():
    print("Creating sample categories...")

    # Create categories
    categories_data = [
        {'name': 'makeup', 'slug': 'makeup', 'description': 'Beauty and cosmetic products'},
        {'name': 'ladies_shoes', 'slug': 'ladies-shoes', 'description': 'Stylish shoes for women'},
        {'name': 'gents_shoes', 'slug': 'gents-shoes', 'description': 'Quality shoes for men'},
        {'name': 'ladies_dresses', 'slug': 'ladies-dresses', 'description': 'Elegant dresses for women'},
        {'name': 'gents_dresses', 'slug': 'gents-dresses', 'description': 'Formal wear for men'},
        {'name': 'accessories', 'slug': 'accessories', 'description': 'Fashion accessories and jewelry'},
    ]

    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'slug': cat_data['slug'],
                'description': cat_data['description']
            }
        )
        if created:
            print(f"Created category: {category.name}")
        else:
            print(f"Category already exists: {category.name}")

    print("\nCreating sample products...")

    # Create sample products
    products_data = [
        {
            'name': 'Lipstick Set',
            'slug': 'lipstick-set',
            'description': 'High-quality lipstick set with various shades',
            'price': 24.99,
            'category': 'makeup',
            'stock': 50
        },
        {
            'name': 'Foundation',
            'slug': 'foundation',
            'description': 'Smooth and long-lasting foundation',
            'price': 19.99,
            'category': 'makeup',
            'stock': 30
        },
        {
            'name': 'High Heel Shoes',
            'slug': 'high-heel-shoes',
            'description': 'Elegant high heel shoes for special occasions',
            'price': 89.99,
            'category': 'ladies_shoes',
            'stock': 20
        },
        {
            'name': 'Leather Loafers',
            'slug': 'leather-loafers',
            'description': 'Comfortable leather loafers for men',
            'price': 79.99,
            'category': 'gents_shoes',
            'stock': 15
        },
        {
            'name': 'Evening Dress',
            'slug': 'evening-dress',
            'description': 'Beautiful evening dress for special events',
            'price': 149.99,
            'category': 'ladies_dresses',
            'stock': 10
        },
        {
            'name': 'Business Suit',
            'slug': 'business-suit',
            'description': 'Professional business suit for men',
            'price': 299.99,
            'category': 'gents_dresses',
            'stock': 8
        },
        {
            'name': 'Designer Handbag',
            'slug': 'designer-handbag',
            'description': 'Premium designer handbag',
            'price': 199.99,
            'category': 'accessories',
            'stock': 12
        },
        {
            'name': 'Sunglasses',
            'slug': 'sunglasses',
            'description': 'Stylish sunglasses with UV protection',
            'price': 49.99,
            'category': 'accessories',
            'stock': 25
        },
    ]

    for prod_data in products_data:
        product, created = Product.objects.get_or_create(
            name=prod_data['name'],
            defaults={
                'slug': prod_data['slug'],
                'description': prod_data['description'],
                'price': prod_data['price'],
                'category': prod_data['category'],
                'stock': prod_data['stock'],
                'available': True
            }
        )
        if created:
            print(f"Created product: {product.name}")
        else:
            print(f"Product already exists: {product.name}")

    print("\nSample data creation completed!")

if __name__ == '__main__':
    create_sample_data()