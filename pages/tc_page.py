from selenium.webdriver.common.by import By
from pages.base_page import Page


class TermsAndConditionsPage(Page):
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='page-title']")

    def verify_tc_page(self):
        self.wait_until_visible(self.PAGE_TITLE)
        self.verify_text('Terms & Conditions', *self.PAGE_TITLE)
        self.verify_partial_url('terms-conditions')