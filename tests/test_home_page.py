import pytest
from pytest_bdd import scenario
from step_definitions.given import *
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('DB-013', 'DB-014', 'DB-015')
@scenario('features/home_page.feature', 'Select Category')
def test_categories():
    pass
