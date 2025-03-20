import time

import allure
from pages.base_page import BasePage
from locators.personal_accoount_locators import PersonalAccountLocators

class PersonalAccountPage(BasePage):
    @allure.step('Нажать на кнопку Личный кабинет')
    def click_personal_account(self):
        self.find_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT).click()
        self.wait_for_load_element(PersonalAccountLocators.TEXT_LOGIN)