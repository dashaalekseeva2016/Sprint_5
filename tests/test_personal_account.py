import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By
from constants import DEFAULT_WAIT
from urls import *
from data import Credentials

class TestPersonalAccount:
    
    def test_navigate_to_personal_account(self, driver_main_page):

        wait = WebDriverWait(driver_main_page, DEFAULT_WAIT)
        driver = driver_main_page

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(Locators.PROFILE_TITLE))
        
        assert "account" in driver.current_url


    def test_navigate_from_account_to_constructor(self, driver_main_page):
        wait = WebDriverWait(driver_main_page, DEFAULT_WAIT)
        driver = driver_main_page

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        order_text = (wait.until(EC.visibility_of_element_located(Locators.CREATE_ORDER))).text
        assert order_text == "Оформить заказ" 
        assert driver.current_url == MAIN_PAGE


    def test_navigate_from_account_to_logo(self, driver_main_page):
        wait = WebDriverWait(driver_main_page, DEFAULT_WAIT)
        driver = driver_main_page

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGO).click()

        order_text = (wait.until(EC.visibility_of_element_located(Locators.CREATE_ORDER))).text
        assert order_text == "Оформить заказ" 
        assert driver.current_url == MAIN_PAGE
