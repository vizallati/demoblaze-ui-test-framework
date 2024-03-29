import os
import allure
import pytest
from selenium import webdriver
from dsl.pages.cart import CartPage
from dsl.pages.home import HomePage
from dsl.pages.sign_up import SignUp
from dsl.pages.contact import Contact
from dsl.pages.sign_in import SignIn
from dsl.pages.about_us import AboutUs
from dsl.pages.product import ProductPage
from allure_commons import plugin_manager
from core.base_actions import BaseActions
from dsl.pages.place_order import PlaceOrder
from allure_pytest_bdd.pytest_bdd_listener import PytestBDDListener
from core.utils import load_yaml, Context, add_tags_allure, add_links_allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope='class', autouse=True)
def load_config():
    """Fixture for loading config files used by tests to memory."""
    load_yaml('settings.yml')
    load_yaml('locators.yml')


@pytest.fixture(scope='class', autouse=True)
def initialize_webdriver():
    """Fixture for initializing webdriver browser instance with given options"""
    if os.getenv('BROWSER') == 'Edge':
        options = EdgeOptions()
        # options.add_argument('--headless')
        options.add_argument('--start-maximized')
        Context.browser = webdriver.Edge(options=options)
    else:
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        Context.browser = webdriver.Chrome(options=chrome_options)

    yield

    Context.browser.close()


@pytest.fixture(autouse=True)
def init_classes():
    """Fixture for initializing instances of various classes used by the tests."""
    Context.base_actions = BaseActions(Context.browser)
    Context.sign_up = SignUp(Context.browser)
    Context.sign_in = SignIn(Context.browser)
    Context.about_us = AboutUs(Context.browser)
    Context.contact = Contact(Context.browser)
    Context.home_page = HomePage(Context.browser)
    Context.product_page = ProductPage(Context.browser)
    Context.cart = CartPage(Context.browser)
    Context.place_order = PlaceOrder(Context.browser)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    pytest hook function to customize the Allure report for BDD scenarios.

    This hook is triggered after the test item has been executed, and it customizes the Allure report by:
    1. Retrieving the test result and setting it in the global `settings.test_result`.
    2. Adding tags to the Allure report based on pytest markers.
    3. Adding links to the Allure report based on test case IDs.
    4. Setting the description of the test result in the Allure report.

    Parameters:
    - item: The pytest item object.

    Returns:
    None
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        for plugin in plugin_manager.list_name_plugin():
            p = plugin[1]
            if isinstance(p, PytestBDDListener):
                Context.test_result = p.lifecycle._get_item()
                add_tags_allure(item)
                add_links_allure()
                # add description to allure report
                Context.test_result.description = Context.test_result.name


def pytest_bdd_before_scenario(request, feature, scenario):
    """
    Set up actions to be performed before each BDD scenario.
    Parameters:
        - request: pytest request object
        - feature: pytest_bdd feature object
        - scenario: pytest_bdd scenario object

    Returns:
        None
    """
    Context.pytest_bdd_step_error = False


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """
    Handle errors that occur during BDD step execution.
    Capture a screenshot if an exception is raised, and attach it to the allure report.

    Parameters:
        - request: pytest request object
        - feature: pytest_bdd feature object
        - scenario: pytest_bdd scenario object
        - step: pytest_bdd step object
        - step_func: BDD step function
        - step_func_args: arguments passed to the step function
        - exception: the exception raised during step execution

    Returns:
        None
    """
    Context.pytest_bdd_step_error = True
    Context.browser.save_screenshot(f'{request.node.name}.png')
    allure.attach.file(source=f'{request.node.name}.png', name=f'{request.node.name}',
                       attachment_type=allure.attachment_type.PNG)
