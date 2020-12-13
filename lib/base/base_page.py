import os
uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
ROOT_DIR = uppath(__file__, 3)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.support.select import Select
from utilities.logger_wrapper import Logger
import logging
import time

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.page_load_timeout = 30
        self.timeout = 20

        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.set_page_load_timeout(self.page_load_timeout)

        self.log = self.start_logger()
        self.retries = 2

    def open(self, base_url):
        self.log.info(f"Open URL: {base_url}\n")
        self.driver.get(base_url)

    def start_logger(self):
        logger_name = "automation"
        log_path = os.path.join(ROOT_DIR, 'output/logs')

        log_filename = "{}/{}.log".format(log_path, logger_name)
        logger_instance = Logger(logger_name)

        log = logger_instance.setup_logger(log_file=log_filename,
                                           log_type=1,
                                           log_level=logging.DEBUG)
        return log

    def locator_type(self, loc_type):
        if loc_type == "xpath":
            return By.XPATH
        if loc_type == 'id':
            return By.ID
        if loc_type == "name":
            return By.NAME
        if loc_type == "css":
            return By.CSS_SELECTOR
        if loc_type == "link text":
            return By.LINK_TEXT
        if loc_type == "class":
            return By.CLASS_NAME
        if loc_type == "tag name":
            return By.TAG_NAME

    def find_element_present(self, locator, loc_type="xpath"):
        by_type = self.locator_type(loc_type)

        i = 0
        element = None
        while i < self.retries:
            try:
                element = WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((by_type, locator)))
                break
            except:
                self.refresh()
                time.sleep(2)
            i = i+1

        if not element:
            error_message = f'TimeoutException: element {locator} not found'
            self.log.error(error_message, exc_info = True)
            raise Exception(error_message)

        return element

    def click(self, locator, loc_type="xpath"):
        element = self.find_element_present(locator, loc_type)

        try:
            element.click()
            time.sleep(2)
        except exceptions.ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator, loc_type = "xpath"):
        return self.find_element_present(locator, loc_type).text

    def refresh(self):
        self.driver.refresh()

    def find_multiple_elements(self, locator, loc_type="xpath"):
        by_type = self.locator_type(loc_type)
        i = 0
        element_list = []

        while i < self.retries:
            try:
                element_list = WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_all_elements_located((by_type, locator)))
                break
            except:
                self.refresh()
                time.sleep(2)
            i = i + 1

        if not element_list:
            error_message = f'TimeoutException: element {locator} not found'
            self.log.error(error_message, exc_info = True)
            raise Exception(error_message)

        return element_list

    def find_select_element(self, locator, loc_type="xpath"):
        element = self.find_element_present(locator, loc_type)
        select = Select(element)
        return select

    def get_all_select_option(self, locator, loc_type="xpath"):
        select = self.find_select_element(locator, loc_type)
        return select.options

    def select_element_by_visible_text(self, value, locator, loc_type="xpath"):
        select = self.find_select_element(locator, loc_type)

        try:
            select.select_by_visible_text(str(value))
            time.sleep(1)

        except Exception as e:
            self.log.error(e)
            raise Exception(e)

    def close(self):
        self.driver.close()
        self.driver.quit()
