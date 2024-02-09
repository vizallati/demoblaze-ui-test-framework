from selenium.webdriver.common.by import By
from core.base_actions import BaseActions
from core.utils import Context


class SignUp(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Context.locators['pop_ups']['sign_up']

    def create_account(self, username, password):
        if username is None:
            self.send_keys(By.XPATH, self.locators['password_field'], password)
        elif password is None:
            self.send_keys(By.XPATH, self.locators['username_field'], username)
        else:
            self.send_keys(By.XPATH, self.locators['username_field'], username)
            self.send_keys(By.XPATH, self.locators['password_field'], password)
        alert_message = self.click_sign_up_button()
        return alert_message

    def close_pop_up(self):
        self.click_on_element(By.XPATH, self.locators['close_button'])

    def click_sign_up_button(self):
        self.click_on_element(By.XPATH, self.locators['signup_button'])
        alert = self.wait_for_alert()
        alert_message = alert.text
        alert.accept()
        return alert_message
