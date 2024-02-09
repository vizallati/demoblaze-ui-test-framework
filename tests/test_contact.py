import pytest
from pytest_bdd import scenario
from step_definitions.given import *
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('DB-012')
@scenario('features/contact.feature', 'Send message')
def test_contact_form():
    pass
