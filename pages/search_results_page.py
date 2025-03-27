from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    ADD_TO_CART_BTN_IN_PRODUCT = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
    PRODUCTS_LIST = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    RESULTS_CATEGORY_NAME = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] > span")

    def click_addToCart_btn_on_product(self):
        products_list = self.wait_until_all_are_visible(self.PRODUCTS_LIST)
        product = products_list[0]
        self.wait_until_clickable(self.ADD_TO_CART_BTN_IN_PRODUCT)
        product.find_element(*self.ADD_TO_CART_BTN_IN_PRODUCT).click()

    def verify_search_results(self, search_word):
        self.verify_partial_text(search_word, *self.RESULTS_CATEGORY_NAME)

    def verify_search_url(self, search_word):
        self.verify_partial_url(search_word)
