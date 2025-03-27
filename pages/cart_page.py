from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_ITEM = (By.CSS_SELECTOR, "[data-test='cart-item-groups']")
    CART_ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='cartItem-price']")
    CART_SUBTOTAL = (By.CSS_SELECTOR, "[data-test='cart-summary-subTotal'] > div:nth-child(2) > p")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] > h1")

    def verify_cart_content(self):
        item = self.wait_until_all_are_visible(self.CART_ITEM)
        assert len(item) == 1, 'Item not found in cart'
        first_item = item[0]
        first_item_price = first_item.find_element(*self.CART_ITEM_PRICE).text
        subtotal = self.find_element(*self.CART_SUBTOTAL).text
        assert first_item_price.strip() == subtotal.strip(), 'Subtotal is incorrect or missing'

    def verify_empty_cart_msg(self):
        self.wait_until_visible(self.EMPTY_CART_MSG)
        self.verify_text('Your cart is empty', *self.EMPTY_CART_MSG)
