from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_forma')
    REGISTER_FORM = (By.ID, 'register_forma')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_TITLE = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADDITION_MESSAGE = (By.ID, 'messages')
    PRODUCT_TITLE_IN_MESSAGE = (
        By.CSS_SELECTOR, '#messages div:first-child .alertinner strong')
    PRODUCT_PRICE_IN_MESSAGE = (
        By.CSS_SELECTOR, '#messages div:nth-child(3) p:first-child strong')
