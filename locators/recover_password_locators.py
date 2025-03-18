from selenium.webdriver.common.by import By

class RecoveryPasswordLocators:
    BUTTON_RECOVERY_PASSWORD = [By.XPATH, './/a[text() = "Восстановить пароль"]']
    FIELD_EMAIL = [By.XPATH,'//label[text() = "Email"]/following-sibling::input']
