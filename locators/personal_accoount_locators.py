from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    BUTTON_PERSONAL_ACCOUNT = [By.XPATH, '//*[@href = "/account"]']
    TEXT_LOGIN = [By.XPATH,"//h2[text()='Вход']"]
    BUTTON_LOGIN = [By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]
    BUTTON_HISTORY_ORDER = [By.XPATH,
                      '//div[contains(@class, "OrderHistory_textBox__3lgbs")]/p[contains(@class, '
                      '"text text_type_digits-default")])[last()]']