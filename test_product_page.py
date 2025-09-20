import pytest
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear" 
    page = ProductPage(browser, link) 
    page.open() 
    page.should_be_add_to_basket_button()    # проверяю, что кнопка есть
    page.add_product_to_basket()             # кликаю + решаем алерт
            
   # page.should_be_add_to_basket_item()      # проверяю, что товар ВООБЩЕ добавлен в корзину
   # page.should_be_add_exact_item()          # проверяю, что КОНКРЕТНЫЙ товар добавился в корзину


