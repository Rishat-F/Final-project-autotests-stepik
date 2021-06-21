from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        collected_errors = []
        try:
            self.should_be_login_url()
        except AssertionError as err:
            collected_errors.append(str(err))
        try:
            self.should_be_login_form()
        except AssertionError as err:
            collected_errors.append(str(err))
        try:
            self.should_be_register_form()
        except AssertionError as err:
            collected_errors.append(str(err))
        assert not collected_errors,
            f"It's not login page! There next problems: {' '.join(collected_errors)}"

    def should_be_login_url(self):
        assert 'bogin' in self.browser.current_url,\
            r"Page hasn't login url!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "There is no login form on page!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),\
            "There is no register form on page!"
