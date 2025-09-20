from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BASKET = (By. CSS_SELECTOR, ".btn-add-to-basket")
    
    # NAME_ITEM = (By.CSS_SELECTOR, ".product_main h1")
    # ITEM_IN_BASKET = (By. CSS_SELECTOR, "#messages .alertinner")
    
    