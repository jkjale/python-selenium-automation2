from utils.wait_utils import WaitUtils


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WaitUtils.wait_for_element_to_be_visible(self.driver.wait, locator)

    def find_elements(self, *locator):
        self.driver.find_elements(*locator)

    def click(self, locator):
        WaitUtils.wait_for_element_to_be_clickable(self.driver.wait, locator).click()

    def input_text(self, text, locator):
        WaitUtils.wait_for_element_to_be_visible(self.driver.wait, locator).send_keys(text)
