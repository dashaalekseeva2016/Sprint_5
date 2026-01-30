from selenium.webdriver.common.by import By

class Locators:
    #регистрация, авторизация
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт"
    REGISTER_LINK = ((By.LINK_TEXT, "Зарегистрироваться")) #ссылка "Зарегестрироваться"
    REG_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input") #поле Имя для регестарции
    REG_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") #поле email для регистрации
    REG_PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']") #поле пароль для регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка "Зарегестрироваться"
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']") #заголовок Вход окна авторизации
    PASSWORD_ERROR = (By.XPATH, "//*[text()='Некорректный пароль']") #ошибка при вводе невалидного пароля или неправильных данных

    #локатроры входа
    CREATE_ORDER = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")#соберите заказ
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']") #заголовок конструктора
    LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']") #отправка формы входа
    LOGIN_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") #поле логина
    LOGIN_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") #поле пароля
    LOGIN_LINK = (By.LINK_TEXT, "Войти") # ссылка на вход
    FORGOT_PASSWORD_LOGIN_LINK = (By.XPATH, "//a[@href='/forgot-password']") #поле восстановление пароля
    FORGOT_PASSWORD_ENTER_LINK = (By.XPATH, "//a[@href='/login']")
    LOGIN_ERROR = (By.CSS_SELECTOR, ".input__error") # ошибка при вводе некорректных данных
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") #кнопка Личный кабинет

    #личный кабинет
    PROFILE_TITLE = (By.XPATH, "//a[@href='/account/profile']") #раздел Профиль на личной странице
    PROFILE_NAME_TEXT = (By.XPATH, "//div[contains(text(), 'Имя')]/following-sibling::div") #имя пользователя
    PROFILE_EMAIL_TEXT = (By.XPATH, "//div[contains(text(), 'Логин')]/following-sibling::div") #email пользователя
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']") #кнопка "Сохранить"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") #кнопка "Выход"
    PROFILE_PASSWORD = (By.XPATH, "//input[@type='password']") #пароль пользователя

    #конструктор
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]") #логотип
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") #
    CONSTRUCTOR_LINK = (By.XPATH, "//a[text()='Конструктор']") #
    BUNS_SECTION = (By.XPATH, '//span[contains(text(), "Булк")]')#секция Булки
    SAUCES_SECTION = (By.XPATH, '//span[contains(text(), "Соус")]')#секция соусы
    FILLINGS_SECTION = (By.XPATH, '//span[contains(text(), "Начинк")]')#секция начинки
    FIRST_SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")#первый соус
    FIRST_FILLING = (By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']")#первая начинка
    FIRST_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")#первая булка
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'current')]") #активный раздел
    
    #выход из аккаунта
    LOGOUT_BUTTON = (By.XPATH, "//button[@class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive']") #кнопка выхода аз аккаунта
