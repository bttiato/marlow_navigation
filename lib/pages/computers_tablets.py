from lib.base.base_page import BasePage
from lib.locators.amazon_locators import computer_tablet_page as ctp
import time

class ComputerTablet(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def get_product_list(self):
        fetch_data = self.find_multiple_elements(
                ctp['product_list_classname'], 'class')

        product_list = []
        for element in fetch_data:
            if element.get_attribute('data-index'):
                product_list.append(element)

        return product_list

    def find_product_by_index(self, index, product_list):

        if len(product_list) <= index:
            msg = f"Total products displayed: {len(product_list)} - " \
                  f"Product requested: {index}th >>> " \
                  f"The {index}th product is not existed in the list"
            self.log.error(msg)
            raise Exception(msg)

        product_link = self.find_multiple_elements(
            ctp['product_link'].format(index-1))[0]

        return product_link

    def get_product_detail(self, product_link):
        product_link.click()
        time.sleep(2)

        product_detail = {}
        msg = "Product is not available in stock at this moment. " \
              "Can't add to cart"
        try:
            product_detail['availability'] = self.get_text(ctp['availability'])
        except:
            self.log.error(msg)
            raise Exception(msg)

        if 'in stock' not in product_detail['availability'].lower():
            self.log.error(msg)
            raise Exception(msg)

        try:
            quantity = self.get_all_select_option(ctp['product_quantity'])
            product_detail['product_quantity'] = len(quantity)
        except Exception as e:
            message = "No quantity information of the product displayed"
            self.log.error(f'{message} -- {e}')
            raise Exception(f'{message}')

        price = self.get_text(ctp['product_price'])[1:]
        product_detail['product_price'] = float(price.replace(',',''))
        product_detail['product_title'] = self.get_text(ctp['product_title'])

        return product_detail

    def add_to_cart(self, quantity, product_detail):
        try:
            add_to_cart_element = self.find_element_present(ctp['add_to_card_id'], "id")
        except Exception as e:
            self.log.error("Add To Cart element not found. Cant add item to "
                           "cart")
            raise e

        if int(product_detail['product_quantity']) < int(quantity):
            message = "Total product orders exceed the quanity of product in " \
                      "stock"
            self.log.info(message)
            raise Exception(message)

        self.select_element_by_visible_text(quantity, ctp['product_quantity'])
        add_to_cart_element.click()
        time.sleep(2)

        self.log.info(f"Added product to cart")

