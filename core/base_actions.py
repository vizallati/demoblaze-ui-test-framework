from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from core.constants import Timeout
import logging


class BaseActions:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, web_element):
        """
        This function finds a web-element
        :param by: method to locate web-element
        :param web_element: locator
        :return: returns a web-element
        """
        try:
            element = self.driver.find_element(by, web_element)
            logging.info(f'Web-element successfully returned: {web_element}')
            return element
        except Exception as error:
            logging.error(error)
            raise error

    def wait_for_element(self, by, web_element, max_retries=3):
        """
        This method waits for a web-element to be present in the DOM with retry mechanism
        :param by: method to locate web-element
        :param web_element: locator
        :param max_retries: maximum number of retries
        """
        for retry in range(max_retries):
            try:
                element = WebDriverWait(self.driver, Timeout.LONG_ELEMENT_WAIT.value).until(
                    expected_conditions.element_to_be_clickable((by, web_element)))
                logging.info(f'Successfully waited for web-element: {web_element}')
                return element
            except TimeoutException:
                if retry < max_retries - 1:
                    # self.driver.refresh()
                    logging.info(f'Retrying ({retry + 1}/{max_retries}) after page refresh...')
                else:
                    logging.error(f'Failed to locate web-element: {web_element} after {max_retries} retries')
                    raise

    def click_on_element(self, by, web_element):
        """
        This function clicks on a web-element
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            element_to_click = self.wait_for_element(by, web_element)
            element_to_click.click()
            logging.info(f'Successfully clicked on web-element: {web_element}')
        except Exception as e:
            logging.error(e)
            raise e

    def send_keys(self, by, web_element, text, max_retries=3):
        """
        This function sets keys to a field
        :param by: method to locate web-element
        :param web_element: locator
        :param text: text to enter
        :param max_retries: maximum number of retries
        """
        for retry in range(max_retries):
            try:
                element_to_send_keys = self.wait_for_element(by, web_element)
                element_to_send_keys.send_keys(text)
                logging.info(f'Successfully set text on web-element: {web_element}')
                break
            except Exception as error:
                logging.error(error)
                if retry < max_retries:
                    self.driver.refresh()
                    logging.info('Refreshing the page and retrying...')
                else:
                    raise error

    def navigate_to_url(self, url):
        """
        This function helps navigate to a new url
        :param url: Url to navigate to
        """
        try:
            self.driver.get(url)
            logging.info(f'Successfully navigated to URL: {url}')
        except Exception as error:
            logging.error(error)
            raise error

    def clear_text(self, by, web_element):
        """
        This function clears text in a field
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            element_to_clear = self.wait_for_element(by=by, web_element=web_element)
            element_to_clear.clear()
            logging.info(f'Successfully cleared text on web-element: {web_element}')
        except Exception as error:
            logging.error(error)
            raise error

    def wait_for_alert(self, timeout=6):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.alert_is_present())

    def refresh_page(self):
        self.driver.refresh()

    def get_element_text(self, by, web_element):
        """
        This function gets the text embedded in a web-element
        :param by: method to locate web-element
        :param web_element: locator
        :return: returns text
        """
        try:
            element = self.wait_for_element(by=by, web_element=web_element)
            text = element.text
            logging.info(f'Successfully returned web-element text: {web_element}')
            return text
        except Exception as error:
            logging.error(error)
            raise error
