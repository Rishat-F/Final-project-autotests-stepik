import time

from .pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'\
       'the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.is_added_to_basket_message_correct()
