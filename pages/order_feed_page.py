import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):

    @allure.step('Нажать на заказ')
    def click_order(self):
        self.wait_for_load_element(OrderFeedLocators.ORDER)
        self.find_element(OrderFeedLocators.ORDER).click()
    @allure.step('Отображение модального окна с деталями заказа')
    def order_modal_is_displayed(self):
        return self.find_element(OrderFeedLocators.ORDER_MODAL_WINDOWN).is_displayed()

    @allure.step('Получить номер последнего заказа')
    def get_last_order_number(self):
        self.wait_for_load_element(OrderFeedLocators.LAST_ORDER)
        return self.get_text_for_element(OrderFeedLocators.LAST_ORDER)

    @allure.step('Количество заказов за все время')
    def get_count_all_orders(self):
        self.wait_for_load_element(OrderFeedLocators.ALL_ORDERS)
        return self.get_text_for_element(OrderFeedLocators.ALL_ORDERS)

    @allure.step('Количество заказов за сегодня')
    def get_count_today_orders(self):
        self.wait_for_load_element(OrderFeedLocators.FOR_TODAY_ORDERS)
        return self.get_text_for_element(OrderFeedLocators.FOR_TODAY_ORDERS)