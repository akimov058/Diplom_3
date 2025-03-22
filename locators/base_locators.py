from selenium.webdriver.common.by import By

class BaseLocators:
    FIELD_EMAIL = [By.XPATH,'//label[text() = "Email"]/following-sibling::input']
    FIELD_PASSWORD = [By.XPATH,'//label[text() = "Пароль"]/following-sibling::input']
    BUTTON_PERSONAL_ACCOUNT = [By.XPATH, '//p[text()="Личный Кабинет"]']

