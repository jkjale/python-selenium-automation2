# from utils.wait_utils import WaitUtils
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.target.com/'

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

    def wait_until_clickable(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        )

    def wait_until_clickable_click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        ).click()

    def wait_until_visible(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element not visible by {locator}'
        )

    def wait_until_invisible(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by {locator}'
        )

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected "{expected_text}" is not "{actual_text}"'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected "{expected_text}" not in "{actual_text}"'

    def verify_url(self, expected_url):
        # current_url = self.driver.current_url
        # print(f'current_url: {current_url}')
        # assert expected_url == current_url, f'Expected "{expected_url}" is not "{current_url}"'
        self.wait.until(
            EC.url_to_be(expected_url),
            message=f'URL does not match {expected_url}'
        )

    def verify_partial_url(self, expected_partial_url):
        # current_url = self.driver.current_url
        # print(f'current_url: {current_url}')
        # assert expected_partial_url in current_url, f'Expected "{expected_partial_url}" not in "{current_url}"'
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'URL does not contain {expected_partial_url}'
        )
