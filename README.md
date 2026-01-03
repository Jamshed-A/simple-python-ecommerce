# JAY DEE'S E-Commerce Website

A modern, responsive e-commerce website built with Django for fashion and beauty products.

## Features

- **Modern UI/UX**: Clean, responsive design with Bootstrap
- **Product Categories**: Makeup, Ladies Shoes, Gents Shoes, Ladies Dresses, Gents Dresses, Accessories
- **User Authentication**: Login/Signup functionality
- **Shopping Cart**: Add/remove items, update quantities
- **Checkout Process**: Complete order flow with shipping information
- **Order Management**: Track and view order history
- **Admin Panel**: Manage products, categories, and orders
- **Mobile Responsive**: Works on all device sizes

## Tech Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (default) or PostgreSQL
- **Template Engine**: Django Templates

## Installation

1. **Clone or download the project**:
   ```
   git clone <repository-url>
   cd ecommerce_project
   ```

2. **Create a virtual environment** (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```
   python manage.py createsuperuser
   ```

6. **Load sample data (optional)**:
   ```
   python manage.py loaddata sample_data.json
   ```

7. **Run the development server**:
   ```
   python manage.py runserver
   ```

8. **Access the application**:
   - Frontend: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
ecommerce_project/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md               # This file
├── ecommerce_project/        # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── views.py            # Main views
│   └── wsgi.py
├── apps/                   # Custom Django apps
│   ├── products/           # Product management
│   ├── users/              # User authentication
│   ├── cart/               # Shopping cart
│   └── orders/             # Order management
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
└── db.sqlite3             # SQLite database (default)
```

## Admin Panel

1. Access the admin panel at http://127.0.0.1:8000/admin/
2. Use the superuser credentials created earlier
3. Manage products, categories, users, and orders

## Usage

1. **Browse Products**: Visit the homepage to see all categories
2. **Product Details**: Click on any product to see more details
3. **Add to Cart**: Use the "Add to Cart" button on product pages
4. **View Cart**: Click the cart icon in the navigation bar
5. **Checkout**: Proceed to checkout to complete your order
6. **Order History**: Check your order history in your profile

## Customization

### Adding Categories
1. Go to Admin Panel → Products → Categories
2. Add new categories as needed

### Adding Products
1. Go to Admin Panel → Products → Products
2. Add products with images, descriptions, prices, and stock

### Changing Site Information
1. Edit `ecommerce_project/views.py` to change site name and tagline
2. Update templates in `templates/` for layout changes

## Deployment

For production deployment:

1. **Update settings.py**:
   - Change `DEBUG = False`
   - Set `ALLOWED_HOSTS`
   - Configure production database

2. **Collect static files**:
   ```
   python manage.py collectstatic
   ```

3. **Use a production web server** like Gunicorn or uWSGI

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues, please create an issue in the repository or contact the development team.