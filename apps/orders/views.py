from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.cart.models import Cart, CartItem
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.all():
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        # Create order
        order = Order.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            postal_code=request.POST.get('postal_code'),
            city=request.POST.get('city')
        )

        # Create order items from cart items
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                price=cart_item.product.price,
                quantity=cart_item.quantity
            )

            # Update product stock
            product = cart_item.product
            product.stock -= cart_item.quantity
            if product.stock < 0:
                product.stock = 0
            product.save()

        # Clear the cart
        cart.items.all().delete()

        messages.success(request, f'Order {order.id} created successfully!')
        return redirect('orders:order_detail', order_id=order.id)

    return render(request, 'orders/checkout.html', {'cart': cart})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/list.html', {'orders': orders})