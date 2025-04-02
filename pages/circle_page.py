from selenium.webdriver.common.by import By
from pages.base_page import Page


class CirclePage(Page):
    BENEFIT_CELL = (By.CSS_SELECTOR, ".cell-item-content")

    def verify_number_of_cells_shown(self, count):
        benefit_cells = self.wait_until_all_are_visible(self.BENEFIT_CELL)
        assert len(benefit_cells) >= int(count), f'Did not find at least {count} benefit cells'
