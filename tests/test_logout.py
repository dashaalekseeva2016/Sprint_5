import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators

def test_logout_from_account(driver, registered_user):
    email = registered_user["email"]
    password = registered_user["password"]
    
    driver.get("https://stellarburgers.education-services.ru/")
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_SUBMIT).click()
    wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
    
    wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(EC.url_contains("account"))
    time.sleep(1)
    
    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']")))
    logout_button.click()

    wait.until(EC.url_contains("login"))
    