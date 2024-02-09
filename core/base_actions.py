from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from core.constants import Timeout
import logging


class BaseActions:
    """
      Base class for common actions performed on web elements.

      This class provides methods for interacting with web elements, such as finding elements,
      waiting for elements to be clickable, clicking on elements, sending keys, navigating to URLs,
      waiting for alerts, and getting text from elements.

      Args:
          driver: The WebDriver instance to use for interacting with the browser.

      Attributes:
          driver: The WebDriver instance used for browser interaction.

    """
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, web_element):
        """
        Find and return a web element using the specified locator method and value.

        Args:
            by (str): The method to locate the element, e.g., 'id', 'name', 'xpath'.
            web_element (str): The value of the element locator.

        Returns:
            selenium.webdriver.remote.webelement.WebElement: The located web element.

        Raises:
            Exception: If an error occurs while finding the element.
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
        Waits for a web element to be clickable and returns it.

        Args:
            by (str): The method to locate the element, e.g., 'id', 'name', 'xpath'.
            web_element (str): The value of the element locator.
            max_retries (int, optional): The maximum number of retries (default is 3).

        Returns:
            selenium.webdriver.remote.webelement.WebElement: The located web element.

        Raises:
            TimeoutException: If the element is not found within the specified timeout.
        """

        for retry in range(max_retries):
            try:
                element = WebDriverWait(self.driver, Timeout.LONG_ELEMENT_WAIT.value).until(
                    expected_conditions.element_to_be_clickable((by, web_element)))
                logging.info(f'Successfully waited for web-element: {web_element}')
                return element
            except TimeoutException:
                if retry < max_retries - 1:
                    self.driver.refresh()
                    logging.info(f'Retrying ({retry + 1}/{max_retries}) after page refresh...')
                else:
                    logging.error(f'Failed to locate web-element: {web_element} after {max_retries} retries')
                    raise

    def click_on_element(self, by, web_element):
        """
        Clicks on a web element identified by the specified locator method and value.

        Args:
            by (str): The method to locate the element, e.g., 'id', 'name', 'xpath'.
            web_element (str): The value of the element locator.

        Raises:
            Exception: If an error occurs while clicking the element.
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
        Sends text to a web element identified by the specified locator method and value.

        Args:
            by (str): The method to locate the element, e.g., 'id', 'name', 'xpath'.
            web_element (str): The value of the element locator.
            text (str): The text to send to the element.
            max_retries (int, optional): The maximum number of retries (default is 3).

        Raises:
            Exception: If an error occurs while sending keys to the element.
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
        Navigates the browser to the specified URL.

        Args:
            url (str): The URL to navigate to.

        Raises:
            Exception: If an error occurs while navigating to the URL.
        """

        try:
            self.driver.get(url)
            logging.info(f'Successfully navigated to URL: {url}')
        except Exception as error:
            logging.error(error)
            raise error

    def wait_for_alert(self, timeout=Timeout.SHORT_ELEMENT_WAIT.value):
        """
        Waits for an alert to be present and returns it.

        Args:
            timeout (int, optional): The maximum time to wait for the alert to appear, in seconds (default is 6).

        Returns:
            selenium.webdriver.common.alert.Alert: The located alert object.
        """

        return WebDriverWait(self.driver, timeout).until(expected_conditions.alert_is_present())

    def refresh_page(self):
        self.driver.refresh()

    def get_element_text(self, by, web_element):
        """
        Gets the text content of a web element identified by the specified locator method and value.

        Args:
            by (str): The method to locate the element, e.g., 'id', 'name', 'xpath'.
            web_element (str): The value of the element locator.

        Returns:
            str: The text content of the located web element.

        Raises:
            Exception: If an error occurs while retrieving the text content of the element.
        """

        try:
            element = self.wait_for_element(by=by, web_element=web_element)
            text = element.text
            logging.info(f'Successfully returned web-element text: {web_element}')
            return text
        except Exception as error:
            logging.error(error)
            raise error
