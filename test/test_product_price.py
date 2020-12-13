import sys
import os
uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
ROOT_DIR = uppath(__file__, 2)
sys.path.append(ROOT_DIR)

from utilities import utils
from lib.pages.computers_tablets import ComputerTablet as CT
from lib.pages.menu_navigation import Navigation
from lib.pages.cart_checkout import CartCheckout
import HtmlTestRunner
import unittest
from selenium import webdriver
from parameterized import parameterized
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

TEST_DATA = utils.parse_csv()

def custom_testcase_name(testcase_func, _param_num, param):
    return f"{testcase_func.__name__} " \
           f"[Product_Index: {parameterized.to_safe_name(param.args[0])}; " \
           f"Order_Quantity: {parameterized.to_safe_name(param.args[1])}]"

class TestProductPrice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = utils.parse_config()

        if cls.config['browser'] == 'chrome':
            from selenium.webdriver.chrome.options import Options
            from webdriver_manager.chrome import ChromeDriverManager
            cls.chrome_options = Options()
            cls.chrome_caps = DesiredCapabilities.CHROME
            cls.chrome_caps['pageLoadStrategy'] = 'eager'

            if cls.config['headless']:
                cls.chrome_options.add_argument('window-size=1024,512')
                cls.chrome_options.add_argument('--disable-gpu')
                cls.chrome_options.add_argument('--no-sandbox')
                cls.chrome_options.add_argument('headless')

            cls.driver = webdriver.Chrome(
                executable_path = ChromeDriverManager().install(),
                options=cls.chrome_options, desired_capabilities=cls.chrome_caps)

        cls.computer_tablet = CT(cls.driver)
        cls.menu_navigate = Navigation(cls.driver)
        cls.cart_checkout = CartCheckout(cls.driver)
        cls.computer_tablet.open(cls.config['base_url'])

    @parameterized.expand(TEST_DATA, name_func=custom_testcase_name)
    def test_product_price(self, product_index, quantity):

        tc_desc = f"Go to Computers & Tablets, select product at " \
                  f"index {product_index} and add {quantity} quantities to cart"
        print(f"Test Case Description: {tc_desc}.\n")

        self.computer_tablet.log.info(f"NEW TEST CASE: product_index: "
                                      f"{product_index}, quantity: {quantity}")

        try:
            self.menu_navigate.to_computer_tablet_page()

            product_list = self.computer_tablet.get_product_list()
            product_link = self.computer_tablet.find_product_by_index(
                int(product_index), product_list)
            self.computer_tablet.log.info(f"The {product_index}th product found")

            product_detail = self.computer_tablet.get_product_detail(product_link)

            self.computer_tablet.add_to_cart(int(quantity), product_detail)

            self.cart_checkout.to_cart_checkout()
            product_in_card = self.cart_checkout.cart_products()
            found_product = self.cart_checkout.search_cart_product(product_in_card,
                                                                   product_detail['product_title'])

            price_before = product_detail['product_price']
            price_after = found_product['data_price']
            self.assertEqual(price_before, price_after)

            self.computer_tablet.log.info("Test result: ")
            msg = f"\tProduct's price before added to cart: ${price_before}\n"
            msg += f"\tThe product's price in cart: ${price_after}"
            self.computer_tablet.log.info(msg)

        except Exception as e:
            self.computer_tablet.log.info("===>>> TEST CASE FINISHED <<<===\n\n")
            self.fail(e)

        self.computer_tablet.log.info("===>>> TEST CASE FINISHED <<<===\n\n")

    @classmethod
    def tearDownClass(cls):
        cls.computer_tablet.close()


if __name__ == "__main__":
    outfile = os.path.join(ROOT_DIR, "output/reports")
    runner = HtmlTestRunner.HTMLTestRunner(output=outfile,
                                           report_title="Test Report",
                                           open_in_browser=True,
                                           add_timestamp=False,
                                           combine_reports=True)
    unittest.main(testRunner=runner)