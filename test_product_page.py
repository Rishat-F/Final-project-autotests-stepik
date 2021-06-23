import pytest

from .pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'\
       'coders-at-work_207/?promo=newYear2019'


@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer0',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer1',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer2',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer3',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer4',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer5',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer6',
    pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer7', marks=pytest.mark.xfail(reason="Bug that wouldn't be fixed")),
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer8',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer9'
    ])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.is_added_to_basket_message_correct()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.success_message_should_disappering()
