import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE
from users import TestUsers
from constants import DEFAULT_WAIT
from locators import Locators
from generators import DataGenerator

class TestRegistrationWithNewCredentials:
    def test_success_register(self, driver):
        user_data = TestUsers.get_valid_users()
        name = user_data["name"]
        email = user_data["email"]
        password = user_data["password"]

        wait = WebDriverWait(driver, DEFAULT_WAIT)
        driver.get(MAIN_PAGE)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        wait.until(EC.visibility_of_element_located(Locators.REG_NAME)).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        wait.until(EC.visibility_of_element_located(Locators.LOGIN_TITLE))

        assert "/login" in driver.current_url
       
    def test_registration_with_short_password_error(self, driver):
        user_data = TestUsers.get_user_with_short_password()
        name = user_data["name"]
        email = user_data["email"]
        password = user_data["password"] 

        wait = WebDriverWait(driver, DEFAULT_WAIT)
        driver.get(MAIN_PAGE)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        wait.until(EC.visibility_of_element_located(Locators.REG_NAME)).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        wait.until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
        
        error_element = driver.find_element(*Locators.PASSWORD_ERROR)
        assert error_element.is_displayed()
