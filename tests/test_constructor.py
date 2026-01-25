import pytest
import time
from selenium.webdriver.common.by import By
from locators import Locators

class TestConstructor:
    
    def test_click_sauces_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        time.sleep(3)
        
        driver.find_element(*Locators.SAUCES_SECTION).click()
        time.sleep(1)
        
        active_div = driver.find_element(*Locators.ACTIVE_SECTION)
        assert "Соусы" in active_div.text
    
    def test_click_fillings_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        time.sleep(3)
        
        driver.find_element(*Locators.FILLINGS_SECTION).click()
        time.sleep(1)
        
        active_div = driver.find_element(*Locators.ACTIVE_SECTION)
        assert "Начинки" in active_div.text
    
    def test_click_buns_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        time.sleep(3)
        
        driver.find_element(*Locators.SAUCES_SECTION).click()
        time.sleep(1)
        
        active_div = driver.find_element(*Locators.ACTIVE_SECTION)
        assert "Соусы" in active_div.text
        
        buns_element = driver.find_element(*Locators.BUNS_SECTION)
        buns_element.click()
        time.sleep(1)
        
        active_div = driver.find_element(*Locators.ACTIVE_SECTION)
        assert "Булки" in active_div.text