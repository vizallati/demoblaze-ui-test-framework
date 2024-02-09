import pytest
from pytest_bdd import scenario
from step_definitions.given import *
from step_definitions.when import *
from step_definitions.then import *


@pytest.mark.case_id('DB-006')
@scenario('features/sign_in.feature', 'Login to account')
def test_account_login():
    pass


@pytest.mark.case_id('DB-007')
@scenario('features/sign_in.feature', 'Login without filling username and password')
def test_account_login_no_username_or_password():
    pass


@pytest.mark.case_id('DB-008', 'DB-009')
@scenario('features/sign_in.feature', 'Login without filling one of required values')
def test_account_login_no_fields():
    pass


@pytest.mark.case_id('DB-010')
@scenario('features/sign_in.feature', 'Logout from account')
def test_account_logout():
    pass
