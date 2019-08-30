"""This module allows changing data in user resume"""
import allure
from base import RESUME_URL
from credentials import Credentials
from data_tests.user_data import USER_RESUME, POSITION


@allure.feature('Changing data in user resume')
def test_change_data(app):
    """Changing data in user resume"""

    with allure.step('Login'):
        app.authentication(*Credentials['USER'])

    with allure.step('Changing data'):
        app.put(RESUME_URL, data=USER_RESUME)

    with allure.step('Checking resulttt'):
        assert app.request.status_code == 200
        assert app.request.json()['position'] == POSITION
