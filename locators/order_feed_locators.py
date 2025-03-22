from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER = [By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]']
    ORDER_MODAL_WINDOWN = [By.XPATH, './/div[contains(@class, "Modal_orderBox")]']
    LAST_ORDER = [By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]']
