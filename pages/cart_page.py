from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] > h1")

    def verify_empty_cart_msg(self):
        self.wait_until_visible(self.EMPTY_CART_MSG)
        self.verify_text('Your cart is empty', *self.EMPTY_CART_MSG)
