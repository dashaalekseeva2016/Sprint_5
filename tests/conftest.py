import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from selenium import webdriver
from urls import MAIN_PAGE
import random
import string


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture
def registration_data():
    from generators import DataGenerator
    return DataGenerator.generate_registration_data()

@pytest.fixture
def registered_user(driver, registration_data):
    name, email, password = registration_data
    driver.get("https://stellarburgers.education-services.ru/register")
    
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))).send_keys(name)
    
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH,"//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH,"//button[text()='Зарегистрироваться']").click()
    wait.until(EC.url_contains("login"))
    return {"name": name, "email": email, "password": password}

@pytest.fixture
def registration_data():
    from tests.generators import DataGenerator
    return DataGenerator.generate_registration_data()

@pytest.fixture
def logged_in_user(driver, registration_data):
    name, email, password = registration_data
    
    driver.get("https://stellarburgers.education-services.ru/login")
    
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    wait = WebDriverWait(driver, 15)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))).send_keys(email)
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")))
        print(f"✓ Пользователь {email} успешно залогинен")
    except:
        print(f"✗ Логин не удался, регистрируем {email}")
    
    return {"name": name, "email": email, "password": password}