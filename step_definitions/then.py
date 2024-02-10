from assertpy import assert_that
from pytest_bdd import then, parsers
from selenium.webdriver.common.by import By

from core.constants import EXPECTED_NUMBER_OF_PRODUCTS_PER_PAGE
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


@then(parsers.cfparse('Products are filtered to reflect "{category_option}" category'))
def check_category_selection(category_option, category_items):
    expected_number_of_products = EXPECTED_NUMBER_OF_PRODUCTS_PER_PAGE.get(category_option, 0)
    assert_that(len(category_items)).is_equal_to(expected_number_of_products)


@then("Product page has all required content (picture, product name, description, add to cart button and price)")
def check_product_page_content():
    assert_that(Context.product_page.get_page_content(content='product_name')).is_not_none()
    assert_that(Context.product_page.get_page_content(content='product_price')).is_not_none()
    assert_that(Context.product_page.get_page_content(content='product_image')).is_not_none()
    assert_that(Context.product_page.get_page_content(content='product_description')).is_not_none()
    assert_that(Context.product_page.get_page_content(content='add_to_cart_button')).is_not_none()


@then("Cart page has all the has all required content(total price, place order button, pic, title, price and delete)")
def check_cart_page_content():
    assert_that(Context.cart.get_page_content(content='total_price')).is_not_none()
    assert_that(Context.cart.get_page_content(content='place_order_button')).is_not_none()
    assert_that(Context.cart.get_page_content(content='pic')).is_not_none()
    assert_that(Context.cart.get_page_content(content='title')).is_not_none()
    assert_that(Context.cart.get_page_content(content='price')).is_not_none()
    assert_that(Context.cart.get_page_content(content='delete')).is_not_none()


@then("Order was successfully placed")
def check_order_confirmation():
    assert_that(Context.place_order.get_confirmation_message()).is_not_none()