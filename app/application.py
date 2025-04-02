from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.menu import Menu
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.tc_page import TermsAndConditionsPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.menu = Menu(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.tc_page = TermsAndConditionsPage(driver)