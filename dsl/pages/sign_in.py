from selenium.webdriver.common.by import By
from core.base_actions import BaseActions
from core.utils import Context


class SignIn(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Context.locators['pop_ups']['login']

    def account_login(self, username, password, alert=False):
        if username is None:
            self.send_keys(By.XPATH, self.locators['password_field'], password)
        elif password is None:
            self.send_keys(By.XPATH, self.locators['username_field'], username)
        else:
            self.send_keys(By.XPATH, self.locators['username_field'], username)
            self.send_keys(By.XPATH, self.locators['password_field'], password)
        alert_message = self.click_login_button(alert)
        return alert_message

    def close_pop_up(self):
        self.click_on_element(By.XPATH, self.locators['close_button'])

    def click_login_button(self, alert=False):
        self.click_on_element(By.XPATH, self.locators['login_button'])
        if alert is True:
            alert = self.wait_for_alert()
            alert_message = alert.text
            alert.accept()
            return alert_message

    def get_welcome_message(self):
        return self.get_element_text(By.XPATH, Context.locators['pages']['home_page']['nav_bar']['welcome_message'])

