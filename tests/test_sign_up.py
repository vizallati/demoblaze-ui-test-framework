import pytest
from pytest_bdd import scenario
from step_definitions.given import *
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('DB-001')
@scenario('features/sign_up.feature', 'Create account')
def test_account_creation():
    pass


@pytest.mark.case_id('DB-002')
@scenario('features/sign_up.feature', 'Create account with preexisting username')
def test_create_account_preexisting_username():
    pass


@pytest.mark.case_id('DB-003')
@scenario('features/sign_up.feature', 'Signup without filling username and password')
def test_create_account_no_fields():
    pass


@pytest.mark.case_id('DB-004', 'DB-005')
@scenario('features/sign_up.feature', 'Signup without filling one of required values')
def test_create_account_one_field():
    pass
