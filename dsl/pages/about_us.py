from selenium.webdriver.common.by import By
from core.base_actions import BaseActions
from core.utils import Context


class AboutUs(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Context.locators['pop_ups']['about_us']

    def get_youtube_video(self):
        return self.wait_for_element(By.XPATH, self.locators['youtube_video'])