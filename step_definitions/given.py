from core.utils import Context, generate_username, generate_password
from pytest_bdd import given, parsers
from step_definitions.then import check_account_login
from step_definitions.when import navigate_to_nav_bar_option, fill_in_sign_in_pop_up, select_category, \
    select_product_from_category, add_product_to_cart


@given('I navigate to the homepage')
def navigate_to_homepage():
    Context.base_actions.navigate_to_url(Context.base_url)


@given('I have an account already created')
def create_user_account():
    navigate_to_homepage()
    navigate_to_nav_bar_option(nav_bar_option='sign_up')
    Context.username = generate_username()
    Context.password = generate_password()
    Context.sign_up.create_account(username=Context.username, password=Context.password)
    Context.sign_up.close_pop_up()


@given("I have an account successfully created and logged in")
def create_and_login_account():
    create_user_account()
    navigate_to_nav_bar_option(nav_bar_option='login')
    fill_in_sign_in_pop_up()
    check_account_login()


@given(parsers.cfparse('I have a product with "{category_option}" added to cart'))
def given_add_product_to_cart(category_option):
    navigate_to_homepage()
    category_items = select_category(category_option)
    select_product_from_category(category_option, category_items)
    add_product_to_cart()
