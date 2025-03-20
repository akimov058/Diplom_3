from selenium.webdriver.common.by import By

class RecoveryPasswordLocators:
    BUTTON_RECOVERY_PASSWORD = [By.XPATH, './/a[text() = "Восстановить пароль"]']
    BUTTON_RECOVERY = [By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]
    BUTTON_SHOW_PASSWORD = [By.XPATH,'//div[@class="input__icon input__icon-action"]']
    BUTTON_HIDE_PASSWORD = [By.XPATH,'//label[text()="Пароль"]/parent::div']
