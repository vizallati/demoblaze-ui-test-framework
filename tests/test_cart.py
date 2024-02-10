import pytest
from pytest_bdd import scenario
from step_definitions.given import *
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('DB-022', 'DB-023', 'DB-024')
@scenario('features/cart.feature', 'Check cart content for each category')
def test_cart_page_content():
    pass
