from core.utils import Context, generate_username, generate_password
from pytest_bdd import given

from step_definitions.then import check_account_login
from step_definitions.when import navigate_to_nav_bar_option, navigate_to_nav_bar_option_, fill_in_sign_in_pop_up


@given('I navigate to the homepage')
def navigate_to_homepage():
    Context.base_actions.navigate_to_url('https://www.demoblaze.com/index.html')


@given('I have a user already created')
def create_user():
    navigate_to_homepage()
    navigate_to_nav_bar_option()
    Context.username = generate_username()
    Context.password = generate_password()
    Context.sign_up.create_account(username=Context.username, password=Context.password)
    Context.sign_up.close_pop_up()


@given("I have an account successfully created and logged in")
def create_and_login_account():
    create_user()
    navigate_to_nav_bar_option_()
    fill_in_sign_in_pop_up()
    check_account_login()
