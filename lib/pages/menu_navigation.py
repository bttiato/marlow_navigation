import time
from selenium.common import exceptions
from lib.base.base_page import BasePage
from lib.locators import amazon_locators as al

class Navigation(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.main_page = al.main_page['main_page_logo']

    def to_main_page(self):
        self.click(self.main_page)

    def to_all_menu(self):
        self.click(al.side_navbar_menu['menu_all_id'], "id")

    def expand_all_departments(self):
        all_department_elements = self.find_multiple_elements(
            al.side_navbar_menu['see_all_css'], "css")

        return all_department_elements

    def to_department(self, depart_name, locator, loc_type="xpath"):
        all_departments = self.expand_all_departments()
        found = False

        for see_all in all_departments:
            try:
                self.click(locator, loc_type)
                self.log.info(f"Go to department {depart_name}")
                found = True
                break
            except exceptions.ElementNotInteractableException:
                see_all.click()

        if not found:
            error_message = f'TimeoutException: element {locator} not found'
            self.log.error(error_message, exc_info = True)
            raise Exception(error_message)

    def to_sub_department(self, locators):
        for locator in locators:
            self.click(locator)
            time.sleep(1)

    def to_computer_tablet_page(self):
        self.to_main_page()
        self.to_all_menu()
        self.to_department("Electronics", al.side_navbar_menu['electronics'])

        sub_departments = [al.side_navbar_menu['computer_accessory'],
                           al.side_navbar_menu['computer_tablets']]
        self.to_sub_department(sub_departments)
        self.log.info("Go to 'Computers & Tablets successfully")
