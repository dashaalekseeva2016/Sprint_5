import pytest
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestLogin:
    
    def test_login_from_main_page_button(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
    
    def test_login_from_personal_account_button(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
    
    def test_login_from_registration_page(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        driver.get("https://stellarburgers.education-services.ru/register")
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_LINK)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
    
    def test_login_from_forgot_password_page(self, driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LOGIN_LINK)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
    
    def test_login_with_invalid_credentials(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys("wrong@email.com")
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys("wrongpassword")
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
        
        error_element = driver.find_element(*Locators.PASSWORD_ERROR)
        error_text = error_element.text
        
        assert "Некорректный пароль" in error_text 