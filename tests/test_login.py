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
from urls import *
from data import Credentials

class TestLogin:
    
    def test_login_from_main_page_button(self, driver_main_page):
        wait = WebDriverWait(driver_main_page, DEFAULT_WAIT)
        driver = driver_main_page

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        signin_text = wait.until(EC.visibility_of_element_located(Locators.CREATE_ORDER)).text
        assert signin_text == "Оформить заказ"
        assert driver.current_url == MAIN_PAGE
    
    def test_login_from_personal_account_button(self, driver_main_page):
        wait = WebDriverWait(driver_main_page, DEFAULT_WAIT)
        driver = driver_main_page

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        signin_text = wait.until(EC.visibility_of_element_located(Locators.CREATE_ORDER)).text
        assert signin_text == "Оформить заказ"
        assert driver.current_url == MAIN_PAGE
    
    def test_login_from_registration_page(self, driver_register_page):
        wait = WebDriverWait(driver_register_page, DEFAULT_WAIT)
        driver = driver_register_page
        
        driver.find_element(*Locators.FORGOT_PASSWORD_ENTER_LINK).click()
        
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        signin_text = wait.until(EC.visibility_of_element_located(Locators.CREATE_ORDER)).text
        assert signin_text == "Оформить заказ"
        assert driver.current_url == MAIN_PAGE
    
    def test_login_from_forgot_password_page(self, driver_main_page):
        wait = WebDriverWait(driver_main_page, DEFAULT_WAIT)
        driver = driver_main_page
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_LOGIN_LINK).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_ENTER_LINK).click()

        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        signin_text = wait.until(EC.visibility_of_element_located(Locators.CREATE_ORDER)).text
        assert signin_text == "Оформить заказ"
        assert driver.current_url == MAIN_PAGE
    
    def test_login_with_invalid_credentials(self, driver):
        wait = WebDriverWait(driver, DEFAULT_WAIT)
        driver.get(MAIN_PAGE)
            
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys("wrong@email.com")
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys("wrongpassword")
        driver.find_element(*Locators.LOGIN_SUBMIT).click()


        assert driver.current_url == LOGIN_PAGE
        