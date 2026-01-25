import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By

class TestPersonalAccount:
    
  def test_navigate_to_personal_account(self, driver, registered_user):
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
    current_url = driver.current_url
    assert "account" in current_url, f"URL не содержит 'account'. Текущий URL: {current_url}"


def test_navigate_from_account_to_constructor( driver, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        
        # Вход в систему
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        
        # Переход в личный кабинет
        wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        # Ждем загрузки личного кабинета
        wait.until(EC.url_contains("account"))
        
        # Находим и кликаем на "Конструктор" в шапке
        from selenium.webdriver.common.by import By
        
        constructor_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//header//*[contains(text(), 'Конструктор')]")))
        constructor_element.click()
        
        wait.until(EC.visibility_of_element_located(Locators.MAIN_TITLE))
        
        page_text = driver.find_element(By.TAG_NAME, "body").text
        assert "Соберите бургер" in page_text