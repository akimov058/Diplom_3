import time

import allure
from pages.base_page import BasePage
from locators.recover_password_locators import RecoveryPasswordLocators

class RecoverPasswordPage(BasePage):
    @allure.step('Нажать на кнопку восстановить пароль')
    def click_recovery_password_button(self):
        self.wait_for_load_element(RecoveryPasswordLocators.BUTTON_RECOVERY_PASSWORD)
        self.find_element(RecoveryPasswordLocators.BUTTON_RECOVERY_PASSWORD).click()
    def send_email(self,email):
        self.wait_for_load_element(RecoveryPasswordLocators.FIELD_EMAIL)
        self.find_element(RecoveryPasswordLocators.FIELD_EMAIL).send_keys(email)
