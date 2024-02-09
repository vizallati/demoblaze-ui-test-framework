import time
from pytest_bdd import when, given, parsers
from selenium.webdriver.common.by import By
from core.utils import Context, generate_username, generate_password


@given("I click on the signup option on the navigation bar")
@when("I click on the signup option on the navigation bar")
def navigate_to_nav_bar_option():
    Context.base_actions.click_on_element(By.XPATH, Context.locators['pages']['home_page']['nav_bar']['sign_up'])
    Context.base_actions.wait_for_element(By.XPATH, Context.locators['pop_ups']['sign_up']['label_id'])


@given("I click on the sign in option on the navigation bar")
@when("I click on the sign in option on the navigation bar")
def navigate_to_nav_bar_option_():
    Context.base_actions.click_on_element(By.XPATH, Context.locators['pages']['home_page']['nav_bar']['login'])
    # Context.base_actions.wait_for_element(By.XPATH, Context.locators['pop_ups']['sign_up']['label_id'])


@when("I fill in my username, password and click on the signup button", target_fixture="actual_alert_message")
def fill_in_sign_up_pop_up():
    return Context.sign_up.create_account(username=generate_username(), password=generate_password())


@when("I fill in my username, password and click on the sign in button")
def fill_in_sign_in_pop_up():
    return Context.sign_in.account_login(username=Context.username, password=Context.password)


@when('I try to create account with preexisting username', target_fixture="actual_alert_message")
def create_account_already_used_username():
    Context.sign_up.refresh_page()
    time.sleep(3)
    navigate_to_nav_bar_option()
    return Context.sign_up.create_account(username=Context.username, password=Context.password)


@when("I click signup button without filling in username and password", target_fixture="actual_alert_message")
def click_sign_up_button():
    return Context.sign_up.click_sign_up_button()


@when("I click on the about us option on the navigation bar")
def navigate_to_nav_bar_option_about_us():
    Context.base_actions.click_on_element(By.XPATH, Context.locators['pages']['home_page']['nav_bar']['about_us'])


@when(parsers.cfparse('I fill in only "{required_value}" and click on the signup button'),
      target_fixture="actual_alert_message")
def fill_in_single_value_sign_up(required_value):
    if required_value == 'password':
        return Context.sign_up.create_account(username=None, password=generate_password())
    else:
        return Context.sign_up.create_account(username=generate_username(), password=None)


@when("I click signin button without filling in username and password", target_fixture="actual_alert_message")
def click_sign_up_button():
    return Context.sign_in.click_login_button(alert=True)


@when(parsers.cfparse('I fill in only "{required_value}" and click on the login button'),
      target_fixture="actual_alert_message")
def fill_in_single_value_sign_in(required_value):
    if required_value == 'password':
        return Context.sign_in.account_login(username=None, password=generate_password(), alert=True)
    else:
        return Context.sign_in.account_login(username=generate_username(), password=None, alert=True)


@when("I click on the logout option on the navigation bar")
def navigate_to_nav_bar_option_logout():
    Context.base_actions.click_on_element(By.XPATH, Context.locators['pages']['home_page']['nav_bar']['logout'])


@when("I click on the contact option on the navigation bar")
def navigate_to_nav_bar_option_contact():
    Context.base_actions.click_on_element(By.XPATH, Context.locators['pages']['home_page']['nav_bar']['contact'])


@when(parsers.cfparse('I fill in "{email}", "{name}", "{message}" and click the send message button'), target_fixture="actual_alert_message")
def fill_in_single_value_sign_in(email, name, message):
    return Context.contact.send_message(email, name, message)