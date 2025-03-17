import pytest
from selenium import webdriver

@pytest.fixture(params=['chrome','firefox'])
def driver(requests):
    if requests.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
    elif requests.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()