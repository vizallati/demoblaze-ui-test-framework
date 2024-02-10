from selenium.webdriver.common.by import By
from core.base_actions import BaseActions
from core.utils import Context


class PlaceOrder(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Context.locators['pop_ups']['place_order']

    def fill_in_form(self, **kwargs):
        self.send_keys(By.XPATH, self.locators['name_field'], kwargs.get('customer_name'))
        self.send_keys(By.XPATH, self.locators['country_field'], kwargs.get('country'))
        self.send_keys(By.XPATH, self.locators['city_field'], kwargs.get('city'))
        self.send_keys(By.XPATH, self.locators['card_field'], kwargs.get('credit_card'))
        self.send_keys(By.XPATH, self.locators['month_field'], kwargs.get('month'))
        self.send_keys(By.XPATH, self.locators['year_field'], kwargs.get('year'))
        self.click_purchase_button()
        return self.get_confirmation_message()

    def close_pop_up(self):
        self.click_on_element(By.XPATH, self.locators['close_button'])

    def click_purchase_button(self):
        self.click_on_element(By.XPATH, self.locators['purchase_button'])

    def get_confirmation_message(self):
        confirmation_message = self.wait_for_element(By.XPATH, self.locators['confirmation_message'])
        return confirmation_message


