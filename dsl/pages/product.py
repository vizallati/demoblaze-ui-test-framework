import time

from selenium.webdriver.common.by import By
from core.base_actions import BaseActions
from core.utils import Context


class ProductPage(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Context.locators['pages']['product_page']

    def add_to_cart(self):
        self.click_on_element(By.XPATH, self.locators['add_to_cart_button'])
        alert = self.wait_for_alert()
        alert_message = alert.text
        alert.accept()
        return alert_message

    def get_page_content(self, content):
        category_items = self.wait_for_element(By.XPATH, self.locators[content])
        return category_items
