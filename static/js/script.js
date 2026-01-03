// Add to cart functionality
function addToCart(productId) {
    fetch(`/cart/add/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            'quantity': 1
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            alert('Product added to cart!');
            updateCartCount();
        } else {
            alert('Error adding product to cart: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while adding the product to cart.');
    });
}

// Update cart count in navbar
function updateCartCount() {
    fetch('/cart/count/')
        .then(response => response.json())
        .then(data => {
            const cartCountElement = document.querySelector('.cart-count');
            if(cartCountElement) {
                cartCountElement.textContent = data.count;
            }
        });
}

// Get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Initialize cart count on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
});

// Quantity update in cart
function updateQuantity(itemId, newQuantity) {
    if(newQuantity <= 0) {
        removeItem(itemId);
        return;
    }

    fetch(`/cart/update/${itemId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            'quantity': newQuantity
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            location.reload();
        } else {
            alert('Error updating quantity: ' + data.error);
        }
    });
}

// Remove item from cart
function removeItem(itemId) {
    if(!confirm('Are you sure you want to remove this item from your cart?')) {
        return;
    }

    fetch(`/cart/remove/${itemId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            location.reload();
        } else {
            alert('Error removing item: ' + data.error);
        }
    });
}