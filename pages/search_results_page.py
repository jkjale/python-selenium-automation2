from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULTS_CATEGORY_NAME = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] > span")

    def verify_search_results(self, search_word):
        results_category_name = self.find_element(self.RESULTS_CATEGORY_NAME)
        assert search_word.lower() in results_category_name.text.lower(), 'Results category name not found'

    def verify_search_url(self, search_word):
        assert search_word.lower() in self.driver.current_url.lower(), f'Expected query not in {self.driver.current_url.lower()}'
