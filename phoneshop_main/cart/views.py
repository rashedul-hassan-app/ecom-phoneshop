from django.shortcuts import render, get_object_or_404
from .cart import Cart
from website.models import Product
from django.http import JsonResponse
# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, 'cart_summary.html', {'cart_products': cart_products, 'quantities': quantities})


def cart_add(request):
    print("--- inside the cart_add function ---")
    #  Get the cart object
    cart = Cart(request)

    # test for POST
    if request.POST.get('action') == 'post':
        # Get our product
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product, quantity=product_qty)

        # get the quantity
        cart_quantity = cart.__len__()
        # return the response
        response = JsonResponse(
            {'Product name': product.name, 'qty': cart_quantity})
        return response


def cart_update(request):
    pass


def cart_delete(request):
    pass
