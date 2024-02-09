from selenium.webdriver.common.by import By
from core.base_actions import BaseActions
from core.utils import Context


class Contact(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Context.locators['pop_ups']['contact']

    def send_message(self, email, name, message):
        self.send_keys(By.XPATH, self.locators['email_field'], email)
        self.send_keys(By.XPATH, self.locators['name_field'], name)
        self.send_keys(By.XPATH, self.locators['message_field'], message)
        alert_message = self.click_send_message_button()
        return alert_message

    def close_pop_up(self):
        self.click_on_element(By.XPATH, self.locators['close_button'])

    def click_send_message_button(self):
        self.click_on_element(By.XPATH, self.locators['send_button'])
        alert = self.wait_for_alert()
        alert_message = alert.text
        alert.accept()
        return alert_message

