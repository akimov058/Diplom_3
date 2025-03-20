import allure
from urls.urls import Urls
from pages.personal_account_page import PersonalAccountPage

class TestPersonalAccount:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self,driver):
        driver.get(Urls.URL_BASE_PAGE)
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        assert personal_account.current_url() == Urls.URL_LOGIN_PAGE
