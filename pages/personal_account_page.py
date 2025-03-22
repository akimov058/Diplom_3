import time

import allure
from pages.base_page import BasePage
from locators.personal_accoount_locators import PersonalAccountLocators
from locators.base_locators import BaseLocators
from data.data import Data

class PersonalAccountPage(BasePage):
    @allure.step('Нажать на кнопку Личный кабинет')
    def click_personal_account(self):
        self.wait_for_load_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        self.find_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT).click()
        #self.wait_for_load_element(BaseLocators.FIELD_EMAIL)

    @allure.step('Вводим email')
    def send_email(self):
        self.find_element(BaseLocators.FIELD_EMAIL).send_keys(Data.EMAIL)

    @allure.step('Вводим пароль')
    def send_password(self):
        self.find_element(BaseLocators.FIELD_PASSWORD).send_keys(Data.PASSWORD)

    @allure.step('Нажимаем кнопку Войти')
    def click_button_login(self):
        self.wait_for_load_element(PersonalAccountLocators.BUTTON_LOGIN)
        self.find_element(PersonalAccountLocators.BUTTON_LOGIN).click()
    @allure.step('Авторизация')
    def send_email_and_password_and_login(self):
        self.send_email()
        self.send_password()
        self.click_button_login()
        self.wait_for_load_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
    @allure.step('Нажимаем на кнопку История заказов')
    def click_history_order(self):
        self.wait_for_load_element(PersonalAccountLocators.BUTTON_HISTORY)
        self.find_element(PersonalAccountLocators.BUTTON_HISTORY).click()

    @allure.step('Нажимаем на кнопку Выход')
    def click_logout(self):
        self.wait_for_load_element(PersonalAccountLocators.BUTTON_LOGOUT)
        self.find_element(PersonalAccountLocators.BUTTON_LOGOUT).click()
        self.wait_for_load_element(BaseLocators.FIELD_EMAIL)

