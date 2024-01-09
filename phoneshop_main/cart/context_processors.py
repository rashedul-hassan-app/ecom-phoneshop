from .cart import Cart


def cart(request):
    cart = Cart(request)
    total_quantity = sum(item for item in cart.cart.values())
    return {'cart': Cart(request), 'total_quantity': total_quantity}
