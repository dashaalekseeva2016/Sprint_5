import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By
from constants import DEFAULT_WAIT
from urls import MAIN_PAGE

class TestPersonalAccount:
    
  def test_navigate_to_personal_account(self, driver, registered_user):
    email = registered_user["email"]
    password = registered_user["password"]

    wait = WebDriverWait(driver, DEFAULT_WAIT)
    driver.get(MAIN_PAGE)

    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_SUBMIT).click()

    wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))

    wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(EC.url_contains("account"))
    current_url = driver.current_url
    assert "account" in current_url, f"URL не содержит 'account'. Текущий URL: {current_url}"


def test_navigate_from_account_to_constructor( driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        wait = WebDriverWait(driver, DEFAULT_WAIT)
        driver.get(MAIN_PAGE)
        
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        
        wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        wait.until(EC.url_contains("account"))
        
        
        wait.until(EC.element_to_be_clickable(Locators.LOGO)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        
        assert "stellarburgers" in driver.current_url