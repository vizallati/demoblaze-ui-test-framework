import pytest
from pytest_bdd import scenario
from step_definitions.given import *
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('DB-025', 'DB-026', 'DB-027')
@scenario('features/place_order.feature', 'Place order for each category')
def test_place_order():
    pass
