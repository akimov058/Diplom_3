import time

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
        time.sleep(3)
        self.wait_for_clickable_element(MainFuncLocators.BUTTON_ORDER_FEED)
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

    @allure.step('Нажимаем на крестик')
    def close_ingredient_window(self):
        self.find_element(MainFuncLocators.BUTTON_CLOSE_INGREDIENT_WINDOW).click()

    @allure.step('Получаем текст соберите бургер')
    def get_text_collect_burger(self):
        return self.get_text_for_element(MainFuncLocators.TEXT_COLLECT_BURGER)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient(self):
        self.wait_for_load_element(MainFuncLocators.IMG_INGREDIENT)
        self.drag_and_drop(MainFuncLocators.IMG_INGREDIENT,MainFuncLocators.AREA_BASKET)

    @allure.step('Получаем количество булок')
    def get_count_bun(self):
        time.sleep(2)
        return self.get_text_for_element(MainFuncLocators.TEXT_COUNT_BUN)

    @allure.step('Нажимаем на кнопку оформить заказ')
    def click_button_order(self):
        self.wait_for_load_element(MainFuncLocators.BUTTON_ORDER)
        self.find_element(MainFuncLocators.BUTTON_ORDER).click()

    @allure.step('Проверяем отображение модального окна с номером заказа')
    def check_modal_is_displayed(self):
        self.wait_for_clickable_element(MainFuncLocators.BUTTON_CLOSE_INGREDIENT_WINDOW)
        self.wait_for_load_element(MainFuncLocators.TEXT_ID_ORDER)
        return self.find_element(MainFuncLocators.TEXT_ID_ORDER).is_displayed()

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        self.wait_for_invisibility_element(MainFuncLocators.TEXT_ORDER_NUMBER)
        return self.get_text_for_element(MainFuncLocators.TEXT_ORDER_NUMBER)

    @allure.step('Закрыть модальное окно')
    def click_modal_close(self):
        self.wait_for_load_element(MainFuncLocators.BUTTON_CLOSE_INGREDIENT_WINDOW)
        self.find_element(MainFuncLocators.BUTTON_CLOSE_INGREDIENT_WINDOW).click()