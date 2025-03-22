from selenium.webdriver.common.by import By

class MainFuncLocators:
    BUTTON_CONSTRUCT = [By.XPATH,'//p[text() = "Конструктор"]']
    BUTTON_ORDER_FEED = [By.XPATH,'//p[text() = "Лента Заказов"]']
    IMG_INGREDIENT = [By.XPATH,'(//img[@class="BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4"])[1]']
    TEXT_FOR_MODAL_INGREDIENT = [By.XPATH,'//h2[text() = "Детали ингредиента"]']