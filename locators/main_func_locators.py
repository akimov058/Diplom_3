from selenium.webdriver.common.by import By

class MainFuncLocators:
    BUTTON_CONSTRUCT = [By.XPATH,'//p[text() = "Конструктор"]']
    BUTTON_ORDER_FEED = [By.XPATH,'//p[text() = "Лента Заказов"]']
    IMG_INGREDIENT = [By.XPATH,'(//img[@class="BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4"])[1]']
    TEXT_FOR_MODAL_INGREDIENT = [By.XPATH,'//h2[text() = "Детали ингредиента"]']
    BUTTON_CLOSE_INGREDIENT_WINDOW = [By.XPATH,'//button[contains(@class, "modal__close")]']
    TEXT_COLLECT_BURGER = [By.XPATH,"//h1[@class='text text_type_main-large mb-5 mt-10']"]
    AREA_BASKET = [By.XPATH,'//section[contains(@class, "BurgerConstructor_basket")]']
    TEXT_COUNT_BUN = [By.XPATH,'(//p[contains(@class, "counter_counter__num__3nue1")])[1]']
    BUTTON_ORDER = [By.XPATH,'//button[contains(@class, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg")]']
    TEXT_ID_ORDER = [By.XPATH,'//p[text() = "идентификатор заказа"]']