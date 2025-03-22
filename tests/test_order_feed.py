import allure
from urls.urls import Urls
from pages.main_func_page import MainFuncPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage

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
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        personal_account.send_email_and_password_and_login()
        main_page = MainFuncPage(driver)
        main_page.add_ingredient()
        main_page.click_button_order()
        main_page.check_modal_is_displayed()
        order_number = main_page.get_order_number()
        main_page.click_modal_close()
        main_page.click_order_feed()
        order_page = OrderFeedPage(driver)
        assert order_number in order_page.get_last_order_number()

    @allure.title('При создании нового заказа счетчик Выполнено за все время/сегодня увеличивается')
    def test_count_orders(self, driver):
        driver.get(Urls.URL_BASE_PAGE)
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        personal_account.send_email_and_password_and_login()
        main_page = MainFuncPage(driver)
        main_page.click_order_feed()
        order_page = OrderFeedPage(driver)
        all_orders = order_page.get_count_all_orders()
        today_orders = order_page.get_count_today_orders()
        main_page.click_construct()
        main_page.add_ingredient()
        main_page.click_button_order()
        main_page.check_modal_is_displayed()
        main_page.click_modal_close()
        main_page.click_order_feed()
        new_all_orders = order_page.get_count_all_orders()
        new_today_orders = order_page.get_count_today_orders()
        assert new_all_orders > all_orders and new_today_orders > today_orders







