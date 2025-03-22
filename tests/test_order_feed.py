import allure
from urls.urls import Urls
from pages.main_func_page import MainFuncPage
from pages.order_feed_page import OrderFeedPage

class TestOrderFeed:
    @allure.title('Eсли кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_modal_open(self, driver):
        driver.get(Urls.URL_BASE_PAGE)
        main_func = MainFuncPage(driver)
        main_func.click_order_feed()
        order_feed = OrderFeedPage(driver)
        order_feed.click_order()
        assert order_feed.order_modal_is_displayed() == True

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_from_history_displayed_order_list(self, driver):
        driver.get(Urls.URL_BASE_PAGE)

