from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import ProductPageLocators as ppl


class ProductPage(BasePage):
    @property
    def product_title(self):
        title = self.browser.find_element(*ppl.PRODUCT_TITLE).text.strip()
        return title

    @property
    def product_price(self):
        price = self.browser.find_element(*ppl.PRODUCT_PRICE).text.strip()
        return price.split(' ')[0]

    def add_product_to_basket(self):
        assert self.is_element_present(*ppl.ADD_TO_BASKET_BUTTON),\
            "There is no 'add to basket' button on the product page!"
        add_to_basket_button = self.browser.find_element(
            *ppl.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def is_added_to_basket_message_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_added_to_basket_message_correct(self):
        assert self.is_added_to_basket_message_present(*ppl.ADDITION_MESSAGE),\
            "There is no message after adding product into the basket"
        message = self.browser.find_element(*ppl.SUCCESSFULLY_ADDITION_MESSAGE)
        basket_cost = self.browser.find_element(*ppl.BASKET_COST_MESSAGE)
        assert message.text.strip() ==\
            f'{self.product_title} был добавлен в вашу корзину.',\
            "Product name in message is different from product title!"
        assert basket_cost.text.strip() ==\
            f"Стоимость корзины теперь составляет {self.product_price} £",\
            "Basket cost is different from product price!"
