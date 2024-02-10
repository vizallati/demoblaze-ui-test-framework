import time

from selenium.webdriver.common.by import By
from core.base_actions import BaseActions
from core.utils import Context


class HomePage(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Context.locators['pages']['home_page']

    def select_category(self, category):
        self.click_on_element(By.XPATH, self.locators['categories'][category])

    def get_category_items(self):
        category_items = self.wait_for_elements(By.CSS_SELECTOR, self.locators['category_container'])
        return category_items

