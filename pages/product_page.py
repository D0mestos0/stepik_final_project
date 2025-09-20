from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        print("Ищу кнопку 'Добавить в корзину'")
        add_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        print("Нашла кнопку, кликаю")
        add_basket_button.click()
        print("Кликнула, решаю алерт")
        self.solve_quiz_and_get_code()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "The button 'Add to basket' is not presented"

    def should_be_add_to_basket_item(self):
        # товар ДОБАВЛЕН в корзину
        add_item = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((ProductPageLocators.ITEM_IN_BASKET)))            # жду появления сообщения, что товар добавлен
        add_item_text = add_item.text
        print(f"Текст уведомления: {add_item_text}")
        assert "был добавлен в вашу корзину" in add_item_text, "The item was not added"
        print("Метод should_be_add_to_basket_item выполнен!")

    def should_be_add_exact_item(self):
        # конкретный ТОВАР добавлен в корзину
        name_of_item = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((ProductPageLocators.NAME_ITEM))).text             # жду название в сообщении
        message_item = self.browser.find_element(*ProductPageLocators.ITEM_IN_BASKET).text                                  
        assert name_of_item in message_item,  "The names was not matched"
        
    def should_be_correct_price(self):
        # стоимость товара совпадает со стоимостью корзины
        item_price = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(ProductPageLocators.PRICE_ITEM)).text
        basket_price = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(ProductPageLocators.PRICE_IN_BASKET)).text
        print(f"Цена товара: {item_price}")
        print(f"Цена в уведомлении: {basket_price}")
        assert item_price in basket_price, f"Цена не совпала! Ожидали {item_price}, в корзине {basket_price}"









        # напоминание для меня: лучше найти кнопку еще раз, потому что каждый метод самодостаточен
    
        



    



