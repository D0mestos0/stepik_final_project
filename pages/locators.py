from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_ITEM = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_IN_BASKET = (By.XPATH, "//div[@id='messages']//div[contains(@class,'alert-success')]//div[contains(@class,'alertinner')][contains(., 'был добавлен в вашу корзину')]")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p:first-child strong")
    PRICE_ITEM = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")  # товары в корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")  # текст "Ваша корзина пуста"
