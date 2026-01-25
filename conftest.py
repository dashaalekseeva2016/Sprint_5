import pytest
from selenium import webdriver
from curl import *
import random
import string


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(main_site)
    yield driver
    driver.quit()

def generate_registration_data():
    name = "Дарья Алексеева"
    random_num = random.randint(100, 999)
    email = f"darya_alekseeva_39_{random_num}@yandex.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return name, email, password

@pytest.fixture
def registration_data():
    return generate_registration_data()

@pytest.fixture
def registered_user(driver, registration_data):
    name, email, password = registration_data
    driver.get("https://stellarburgers.education-services.ru/register")
    
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))).send_keys(name)
    
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH,"//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH,"//button[text()='Зарегистрироваться']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    return {"name": name, "email": email, "password": password}

@pytest.fixture
def registration_data():
    from tests.generators import DataGenerator
    return DataGenerator.generate_registration_data()

