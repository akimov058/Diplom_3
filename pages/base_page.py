import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def wait_for_load_element(self,locators):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(locators))

    def find_element(self,locators):
        return self.driver.find_element(*locators)

    def current_url(self):
        return self.driver.current_url
    def execute_scripts(self,element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

