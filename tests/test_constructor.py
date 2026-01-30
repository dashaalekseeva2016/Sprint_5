import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
import time
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import DEFAULT_WAIT
from urls import MAIN_PAGE

class TestConstructor:
    @pytest.mark.parametrize('section_locator, image_locator', [
        (Locators.SAUCES_SECTION, Locators.FIRST_SAUCE),
        (Locators.FILLINGS_SECTION, Locators.FIRST_FILLING)
        ]
    )
    
    def test_constructor_order_sections(self, driver_main_page, section_locator, image_locator):
        wait = WebDriverWait(driver_main_page, DEFAULT_WAIT)
        driver = driver_main_page
        driver.find_element(*section_locator).click()
        assert wait.until(EC.visibility_of_element_located(image_locator))

    def test_constructor_buns_section(self, driver_main_page):
        wait = WebDriverWait(driver_main_page, DEFAULT_WAIT)
        driver = driver_main_page
        driver.find_element(*Locators.SAUCES_SECTION)
        driver.find_element(*Locators.BUNS_SECTION)
        assert wait.until(EC.visibility_of_element_located(Locators.FIRST_BUN))