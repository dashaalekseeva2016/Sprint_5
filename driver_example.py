import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://stellarburgers.education-services.ru/')
time.sleep(30)
driver.quit() 