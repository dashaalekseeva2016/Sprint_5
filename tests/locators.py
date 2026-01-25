from selenium.webdriver.common.by import By

class Locators:
    #регистрация, авторизация
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    REGISTER_LINK = ((By.LINK_TEXT, "Зарегистрироваться"))
    REG_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    REG_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    REG_PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    PASSWORD_ERROR = (By.XPATH, "//*[text()='Некорректный пароль']")

    #локатроры входа
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")
    LOGIN_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    FORGOT_PASSWORD_LOGIN_LINK = (By.LINK_TEXT, "Войти")
    LOGIN_ERROR = (By.CSS_SELECTOR, ".input__error")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    #личный кабинет
    PROFILE_TITLE = (By.XPATH, "//a[text()='Профиль' and contains(@class, 'Account_link')]")
    PROFILE_NAME_TEXT = (By.XPATH, "//div[contains(text(), 'Имя')]/following-sibling::div")
    PROFILE_EMAIL_TEXT = (By.XPATH, "//div[contains(text(), 'Логин')]/following-sibling::div")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_PASSWORD = (By.XPATH, "//input[@type='password']")

    #конструктор
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[text()='Конструктор']")
    BUNS_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span',)
    SAUCES_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span',)
    FILLINGS_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span',)
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'current')]")
    
    #выход из аккаунта
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
