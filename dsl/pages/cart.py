from selenium.webdriver.common.by import By
from core.base_actions import BaseActions
from core.utils import Context


class CartPage(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Context.locators['pages']['cart']

    def place_order(self):
        self.click_on_element(By.XPATH, self.locators['place_order_button'])

    def get_page_content(self, content):
        cart_item = self.wait_for_element(By.XPATH, self.locators[content])
        return cart_item

    def click_place_order_button(self):
        self.click_on_element(By.XPATH, self.locators['place_order_button'])
