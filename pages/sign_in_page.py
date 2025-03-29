from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    email = 'dogbrick@24hinbox.com'
    password = '*****'
    LOGGED_IN_TICKER = (By.CSS_SELECTOR, "#account-sign-in > div > span")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BTN = (By.ID, "login")
    SIGN_IN_PAGE_HEADER = (By.XPATH, "//span[text()='Sign into your Target account']")
    TERMS_AND_CONDITIONS_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")
    USERNAME_FIELD = (By.ID, "username")

    def click_sign_in_btn(self):
        self.click(*self.SIGN_IN_BTN)

    def verify_page_header(self):
        self.verify_partial_text("sign in", *self.SIGN_IN_PAGE_HEADER)

    def verify_password_field(self):
        self.wait_until_visible(self.PASSWORD_FIELD)

    def verify_sign_in_url(self):
        self.verify_partial_url("login")

    def verify_user_is_logged_in(self):
        self.wait_until_invisible(self.USERNAME_FIELD)
        self.wait_until_invisible(self.PASSWORD_FIELD)
        self.verify_url(self.base_url)
        self.wait_until_visible(self.LOGGED_IN_TICKER)

    def verify_username_field(self):
        self.wait_until_visible(self.USERNAME_FIELD)

    def input_username_and_password(self):
        self.input_text(self.email, *self.USERNAME_FIELD)
        self.input_text(self.password, *self.PASSWORD_FIELD)

    def click_target_terms_and_conditions_link(self):
        self.wait_until_clickable_click(self.TERMS_AND_CONDITIONS_LINK)