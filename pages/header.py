from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    SEARCH_FIELD = (By.ID, "search")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")

    def click_cart_icon(self):
        self.wait_until_clickable_click(self.CART_ICON)

    def click_sign_in(self):
        self.wait_until_clickable_click(self.SIGN_IN_BTN)

    def search(self, search_word):
        self.wait_until_clickable(self.SEARCH_FIELD)
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
