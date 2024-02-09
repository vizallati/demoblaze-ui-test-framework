import pytest
from pytest_bdd import scenario
from step_definitions.given import *
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('DB-011')
@scenario('features/about_us.feature', 'View content in about us pop up')
def test_about_us_content():
    pass
