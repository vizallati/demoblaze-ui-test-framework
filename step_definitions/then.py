from assertpy import assert_that
from pytest_bdd import then, parsers
from selenium.webdriver.common.by import By
from core.utils import Context


@then(parsers.cfparse('Alert returns "{expected_alert_message}"'))
def check_account_creation(expected_alert_message, actual_alert_message):
    assert_that(actual_alert_message).is_equal_to(expected_alert_message)


@then("I'm successfully logged into my account")
def check_account_login():
    welcome_message = Context.sign_in.get_welcome_message()
    assert_that(welcome_message).is_equal_to(f'Welcome {Context.username}')


@then("Youtube video should be displayed")
def check_about_us_video():
    assert_that(Context.about_us.get_youtube_video()).is_not_none()


@then("I should be successfully logged out")
def check_account_logout():
    assert_that(Context.sign_in.wait_for_element(By.XPATH,
                                                 Context.locators['pages']['home_page']['nav_bar'][
                                                     'login'])).is_not_none()
