import allure
from urls.urls import Urls
from pages.main_func_page import MainFuncPage
from pages.personal_account_page import PersonalAccountPage


class TestMainFunc:
    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_construct(self,driver):
        driver.get(Urls.URL_LOGIN_PAGE)
        main_func = MainFuncPage(driver)
        main_func.click_construct()
        assert main_func.current_url() == Urls.URL_BASE_PAGE

    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_order_feed(self,driver):
        driver.get(Urls.URL_LOGIN_PAGE)
        main_func = MainFuncPage(driver)
        main_func.click_order_feed()
        assert main_func.current_url() == Urls.URL_ORDER_FEED

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self,driver):
        driver.get(Urls.URL_BASE_PAGE)
        main_func = MainFuncPage(driver)
        main_func.click_ingredient()
        assert main_func.get_text_window_ingredient() == 'Детали ингредиента'

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_click_ingredient_and_close_window(self,driver):
        driver.get(Urls.URL_BASE_PAGE)
        main_func = MainFuncPage(driver)
        main_func.click_ingredient()
        main_func.close_ingredient_window()
        assert main_func.get_text_collect_burger() == 'Соберите бургер'

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_count(self,driver):
        driver.get(Urls.URL_BASE_PAGE)
        main_func = MainFuncPage(driver)
        main_func.add_ingredient()
        assert main_func.get_count_bun() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_create_order_with_login_user(self,driver):
        driver.get(Urls.URL_LOGIN_PAGE)
        personal_account = PersonalAccountPage(driver)
        personal_account.send_email_and_password_and_login()
        main_func = MainFuncPage(driver)
        main_func.add_ingredient()
        main_func.click_button_order()
        assert main_func.check_modal_is_displayed()==True