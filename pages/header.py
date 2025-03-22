from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

    def search(self, search_word):
        self.input_text(search_word, self.SEARCH_FIELD)
        self.click(self.SEARCH_BTN)
