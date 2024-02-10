import pytest
from pytest_bdd import scenario
from step_definitions.given import *
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('DB-016', 'DB-017', 'DB-018')
@scenario('features/product_page.feature', 'Check content of product page for each product category')
def test_product_page_content():
    pass


@pytest.mark.case_id('DB-019', 'DB-020', 'DB-021')
@scenario('features/product_page.feature', 'Add product to cart for each category')
def test_add_product_to_cart():
    pass
