import allure
from urls.urls import Urls
from pages.personal_account_page import PersonalAccountPage
from data.data import Data

class TestPersonalAccount:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self,driver):
        driver.get(Urls.URL_BASE_PAGE)
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        assert personal_account.current_url() == Urls.URL_LOGIN_PAGE

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history(self,driver):
        driver.get(Urls.URL_BASE_PAGE)
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        personal_account.send_email_and_password_and_login()
        personal_account.click_personal_account()
        personal_account.click_history_order()
        assert personal_account.current_url() == Urls.URL_HISTORY_ORDER

    @allure.title('Выход из аккаунта')
    def test_logout(self,driver):
        driver.get(Urls.URL_BASE_PAGE)
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        personal_account.send_email_and_password_and_login()
        personal_account.click_personal_account()
        personal_account.click_logout()
        assert personal_account.current_url() == Urls.URL_LOGIN_PAGE
