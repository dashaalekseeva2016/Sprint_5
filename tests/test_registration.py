import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from generators import DataGenerator
import random

class TestRegistrationWithNewCredentials:
    def test_success_registes(self, driver, registration_data):
        name, email, password = registration_data

        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        wait.until(EC.visibility_of_element_located(Locators.REG_NAME)).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        wait.until(EC.visibility_of_element_located(Locators.LOGIN_TITLE))
        assert "/login" in driver.current_url
       
    def test_registration_with_short_password_error(self, driver):
        name = "Дарья Алексеева"
        random_num = random.randint(100, 999)
        email = f"darya_alekseeva_39_{random_num}@yandex.ru"
        short_password = "12345"  

        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        wait.until(EC.visibility_of_element_located(Locators.REG_NAME)).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(short_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        wait.until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
        
        error_element = driver.find_element(*Locators.PASSWORD_ERROR)
        error_text = error_element.text
        
        assert "Некорректный пароль" in error_text 