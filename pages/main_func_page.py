import allure
from pages.base_page import BasePage
from locators.main_func_locators import MainFuncLocators
from locators.base_locators import BaseLocators
from data.data import Data

class MainFuncPage(BasePage):
    @allure.step('Нажимаем на кнопку Конструктор')
    def click_construct(self):
        self.wait_for_load_element(MainFuncLocators.BUTTON_CONSTRUCT)
        self.find_element(MainFuncLocators.BUTTON_CONSTRUCT).click()
        self.wait_for_load_element(BaseLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Нажимаем на кнопку Лента Заказа')
    def click_order_feed(self):
        self.wait_for_load_element(MainFuncLocators.BUTTON_ORDER_FEED)
        self.find_element(MainFuncLocators.BUTTON_ORDER_FEED).click()
        self.wait_for_load_element(BaseLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Нажимаем на ингредиент')
    def click_ingredient(self):
        self.wait_for_load_element(MainFuncLocators.IMG_INGREDIENT)
        self.find_element(MainFuncLocators.IMG_INGREDIENT).click()
        self.wait_for_load_element(MainFuncLocators.TEXT_FOR_MODAL_INGREDIENT)

    @allure.step('Получаем текст с модального окна с ингредиентами')
    def get_text_window_ingredient(self):
        return self.get_text_for_element(MainFuncLocators.TEXT_FOR_MODAL_INGREDIENT)

