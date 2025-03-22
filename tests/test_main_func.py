import allure
from urls.urls import Urls
from pages.main_func_page import MainFuncPage

class TestMainFunc:
    @allure.title('переход по клику на «Конструктор»')
    def test_go_to_construct(self,driver):
        driver.get(Urls.URL_LOGIN_PAGE)
        main_func = MainFuncPage(driver)
        main_func.click_construct()
        assert main_func.current_url() == Urls.URL_BASE_PAGE

    @allure.title('переход по клику на «Лента заказов»')
    def test_go_to_order_feed(self,driver):
        driver.get(Urls.URL_LOGIN_PAGE)
        main_func = MainFuncPage(driver)
        main_func.click_order_feed()
        assert main_func.current_url() == Urls.URL_ORDER_FEED