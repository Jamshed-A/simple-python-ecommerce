from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from apps.products.models import Product
from .models import Cart, CartItem

def get_or_create_cart(request):
    """Get or create a cart for the user"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # For anonymous users, we could implement session-based cart
        # For now, we'll require login for cart functionality
        return None
    return cart

@login_required
def cart_detail(request):
    cart = get_or_create_cart(request)
    if not cart:
        return redirect('home')

    return render(request, 'cart/detail.html', {'cart': cart})

@login_required
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart = get_or_create_cart(request)

    if not cart:
        return JsonResponse({'success': False, 'error': 'Cart not found'})

    # Get quantity from request
    quantity = int(request.POST.get('quantity', 1))

    # Check if item already exists in cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )

    if not created:
        # If item already exists, update the quantity
        cart_item.quantity += quantity
        cart_item.save()

    return JsonResponse({'success': True, 'message': 'Item added to cart'})

@login_required
@require_POST
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))

    if quantity <= 0:
        cart_item.delete()
    else:
        cart_item.quantity = quantity
        cart_item.save()

    return JsonResponse({'success': True, 'message': 'Cart updated'})

@login_required
@require_POST
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return JsonResponse({'success': True, 'message': 'Item removed from cart'})

@login_required
def cart_count(request):
    """Return the number of items in the cart"""
    cart = get_or_create_cart(request)
    if cart:
        count = cart.items.count()
    else:
        count = 0

    return JsonResponse({'count': count})