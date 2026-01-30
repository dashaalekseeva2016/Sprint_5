import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators
from urls import MAIN_PAGE
from constants import DEFAULT_WAIT
from data import Credentials

class TestLogout:

    def test_logout(self, logged_in_user):
        wait = WebDriverWait(logged_in_user, DEFAULT_WAIT)
        driver = logged_in_user

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(Locators.LOGIN_TITLE))

        assert "/login" in driver.current_url

