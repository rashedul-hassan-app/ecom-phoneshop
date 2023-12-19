from django.shortcuts import render, get_object_or_404
from .cart import Cart
from website.models import Product
from django.http import JsonResponse
# Create your views here.


def cart_summary(request):
    return render(request, 'cart_summary.html', {})


def cart_add(request):
    print("--- inside the cart_add function ---")
    #  Get the cart object
    cart = Cart(request)

    # test for POST
    if request.POST.get('action') == 'post':
        # Get our product
        product_id = int(request.POST.get('product_id'))

        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product)

        # get the quantity
        cart_quantity = cart.__len__()
        # return the response
        response = JsonResponse({'qty': cart_quantity})
        return response


def cart_update(request):
    pass


def cart_delete(request):
    pass
