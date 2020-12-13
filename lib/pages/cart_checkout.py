from lib.base.base_page import BasePage
from lib.locators import amazon_locators as al

class CartCheckout(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def to_cart_checkout(self):
        self.click(al.cart_checkout['to_cart_checkout_id'], "id")
        self.log.info("Go to Cart & Checkout")

    def cart_products(self):
        cart_elements = self.find_multiple_elements(
            al.cart_checkout['cart_item_list_css'], 'css')
        real_products = []

        for ce in cart_elements:
            item_info = {}

            if ce.get_attribute('data-asin'):
                item_info['data_asin'] = ce.get_attribute('data-asin')
                item_info['data_quantity'] = ce.get_attribute('data-quantity')
                item_info['data_price'] = \
                    float(ce.get_attribute('data-price').replace(',',''))
                real_products.append(item_info)

        return real_products

    def search_cart_product(self, added_products, product_title):
        found_product = {}

        self.log.info(f"Check if product '{product_title} is added to cart")
        for product in added_products:
            cart_product_title = self.get_text(
                al.cart_checkout['cart_item_title'].format(product['data_asin']))

            if cart_product_title in product_title:
                found_product = product
                break

        if not found_product:
            raise Exception("Expected product not found in cart")

        self.log.info(f"Product {product_title} is added to cart correctly")
        return found_product
