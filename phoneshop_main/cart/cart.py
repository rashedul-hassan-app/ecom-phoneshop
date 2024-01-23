from website.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # This ensures Cart is available on all of our pages
        self.cart = cart

    def __len__(self):
        # return len(self.cart)
        return sum(item for item in self.cart.values())

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # get cart
        ourcart = self.cart
        ourcart[product_id] = product_qty

        self.session.modified = True
        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)

        # delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def clear(self):
        self.cart.clear()
        self.session.modified = True
        self.session.save()

    def get_prods(self):
        # Get ids from my cart
        product_ids = self.cart.keys()

        # use these ids to lookup Products in database model
        products = Product.objects.filter(id__in=product_ids)

        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def cart_total(self):
        # Get product IDs of all the items in the cart
        product_ids = self.cart.keys()
        # From the IDs, get the actual product so we have access to the prices
        products = Product.objects.filter(id__in=product_ids)
        # Get the quantites out so its easy to calculate
        all_items_in_cart = self.cart
        total = 0

        for key, value in all_items_in_cart.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total
