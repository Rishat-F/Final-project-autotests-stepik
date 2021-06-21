from .pages.main_page import MainPage


link = 'http://selenium1py.pythonanywhere.com/'


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)  # initializing Page Object
    page.open()                     # page opening
    page.should_be_login_link()     # checks is there login link on page


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
