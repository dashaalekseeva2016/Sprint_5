import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import DEFAULT_WAIT
from urls import MAIN_PAGE
from urls import REGISTER_PAGE
from urls import FORGOT_PASSWORD
from selenium.webdriver.common.by import By

class TestLogin:
    
    def test_login_from_main_page_button(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        wait = WebDriverWait(driver, DEFAULT_WAIT)
        driver.get(MAIN_PAGE)
        
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
    
    def test_login_from_personal_account_button(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        wait = WebDriverWait(driver, DEFAULT_WAIT)
        driver.get(MAIN_PAGE)
        
        wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
    
    def test_login_from_registration_page(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        wait = WebDriverWait(driver, DEFAULT_WAIT)
        driver.get(REGISTER_PAGE)
        
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Войти"))).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        assert "stellarburgers" in driver.current_url
    
    def test_login_from_forgot_password_page(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        wait = WebDriverWait(driver, DEFAULT_WAIT)
        driver.get(FORGOT_PASSWORD)
        
        wait.until(EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LOGIN_LINK)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        assert "stellarburgers" in driver.current_url
    
    def test_login_with_invalid_credentials(self, driver):
        wait = WebDriverWait(driver, DEFAULT_WAIT)
        driver.get(MAIN_PAGE)
            
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys("wrong@email.com")
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys("wrongpassword")
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        time.sleep(3)
        assert "login" in driver.current_url, f"Должны быть на странице логина, но URL: {driver.current_url}"
        
        