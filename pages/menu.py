from selenium.webdriver.common.by import By
from pages.base_page import Page


class Menu(Page):
    ADD_TO_CART_BTN_IN_NAV_MENU = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    SIDE_NAV_MENU = (By.XPATH, "//div[@class='ModalDrawer']/div[1]/div[1]")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    VIEWCART_AND_CHECKOUT_BUTTON = (By.XPATH, "//div[@data-test='content-wrapper']/div[3]/a")

    def click_addToCart_btn_in_nav_menu(self):
        self.wait_until_clickable_click(self.ADD_TO_CART_BTN_IN_NAV_MENU)

    def click_sign_in(self):
        self.wait_until_clickable_click(self.SIGN_IN_BTN)

    def click_viewCartAndCheckOut_btn_in_nav_menu(self):
        self.wait_until_clickable_click(self.VIEWCART_AND_CHECKOUT_BUTTON)

    def verify_side_nav_menu(self):
        self.wait_until_visible(self.SIDE_NAV_MENU)
