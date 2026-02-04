import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from selenium import webdriver
from urls import MAIN_PAGE
from urls import REGISTER_PAGE
from urls import LOGIN_PAGE
from locators import Locators
from data import Credentials
import string


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def driver_main_page(driver):
    driver.get(MAIN_PAGE)
    yield driver

@pytest.fixture(scope="function")
def driver_register_page(driver):
    driver.get(REGISTER_PAGE)
    yield driver

@pytest.fixture
def registration_data():
    from generators import DataGenerator
    return DataGenerator.generate_registration_data()

@pytest.fixture
def logged_in_user(driver):
    driver.get(LOGIN_PAGE)     
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_SUBMIT).click()
    yield driver