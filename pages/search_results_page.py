from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULTS_CATEGORY_NAME = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] > span")

    def verify_search_results(self, search_word):
        self.verify_partial_text(search_word, self.RESULTS_CATEGORY_NAME)

    def verify_search_url(self, search_word):
        self.verify_partial_url(search_word)