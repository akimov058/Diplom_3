import allure
from pages.base_page import BasePage
from locators.recover_password_locators import RecoveryPasswordLocators
from locators.base_locators import BaseLocators

class RecoverPasswordPage(BasePage):
    @allure.step('Нажать на кнопку восстановить пароль')
    def click_recovery_password_button(self):
        self.wait_for_load_element(RecoveryPasswordLocators.BUTTON_RECOVERY_PASSWORD)
        self.find_element(RecoveryPasswordLocators.BUTTON_RECOVERY_PASSWORD).click()
    @allure.step('Вводим пароль')
    def send_email(self,email):
        self.wait_for_load_element(BaseLocators.FIELD_EMAIL)
        self.find_element(BaseLocators.FIELD_EMAIL).send_keys(email)
    @allure.step('Нажать на кнопку восстановить')
    def click_recovery_button(self):
        self.find_element(RecoveryPasswordLocators.BUTTON_RECOVERY).click()
        self.wait_for_load_element(BaseLocators.FIELD_PASSWORD)
    @allure.title('Нажать на кнопку показать пароль')
    def click_show_password(self):
        self.find_element(RecoveryPasswordLocators.BUTTON_SHOW_PASSWORD).click()
        self.wait_for_load_element(RecoveryPasswordLocators.BUTTON_HIDE_PASSWORD)

    @allure.step('Проверка, что поля подствечивается')
    def check_show_password(self):
        if ('input_status_active' in self.find_element(RecoveryPasswordLocators.BUTTON_HIDE_PASSWORD).get_attribute('class')):
            return True
        else:
            return False

