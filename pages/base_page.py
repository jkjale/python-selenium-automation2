from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.target.com/'
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_until_clickable(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        )

    def wait_until_clickable_click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def wait_until_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element not visible by {locator}'
        )

    def wait_until_all_are_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator),
            message=f'Elements not visible by {locator}'
        )

    def wait_until_invisible(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by {locator}'
        )

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('Current windows:', all_windows)
        print('Switching to window:', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print('Switching to window:', window_id)
        self.driver.switch_to.window(window_id)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text.strip().lower()
        assert expected_text.lower() == actual_text, f'Expected "{expected_text}" is not "{actual_text}"'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text.lower()
        assert expected_text.lower() in actual_text, f'Expected "{expected_text}" not in "{actual_text}"'

    def verify_url(self, expected_url):
        self.wait.until(
            EC.url_to_be(expected_url),
            message=f'URL does not match {expected_url}'
        )

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'URL does not contain {expected_partial_url}'
        )

    def close(self):
        self.driver.close()
