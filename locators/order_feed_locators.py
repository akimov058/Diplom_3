from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER = [By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]']
    ORDER_MODAL_WINDOWN = [By.XPATH, './/div[contains(@class, "Modal_orderBox")]']
