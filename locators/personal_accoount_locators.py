from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    TEXT_LOGIN = [By.XPATH,"//h2[text()='Вход']"]
    BUTTON_LOGIN = [By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]
    BUTTON_HISTORY = [By.XPATH,'//a[text() = "История заказов"]']
    BUTTON_LOGOUT = [By.XPATH, './/button[text() = "Выход"]']