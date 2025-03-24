import allure
from pages.recover_password_page import RecoverPasswordPage
from urls.urls import Urls
from data.data import Data

class TestRecoveryPassword:
    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_page_forgot_password(self,driver):
        recover_page = RecoverPasswordPage(driver)
        recover_page.open_url(Urls.URL_LOGIN_PAGE)
        recover_page.click_recovery_password_button()
        assert recover_page.current_url() == Urls.URL_FORGOT_PASSWORD

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_send_email_and_click_to_recover_password(self,driver):
        recover_page = RecoverPasswordPage(driver)
        recover_page.open_url(Urls.URL_LOGIN_PAGE)
        recover_page.click_recovery_password_button()
        recover_page.send_email(Data.EMAIL)
        recover_page.click_recovery_button()
        assert recover_page.current_url() == Urls.URL_RESET_PASSWORD

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_to_show_hide_password(self,driver):
        recover_page = RecoverPasswordPage(driver)
        recover_page.open_url(Urls.URL_LOGIN_PAGE)
        recover_page.click_recovery_password_button()
        recover_page.send_email(Data.EMAIL)
        recover_page.click_recovery_button()
        recover_page.click_show_password()
        assert recover_page.check_show_password()