from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    def search(self, search_word):
        self.wait_until_clickable(self.SEARCH_FIELD)
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(self.SEARCH_BTN)

    def click_cart_icon(self):
        self.wait_until_clickable_click(self.CART_ICON)