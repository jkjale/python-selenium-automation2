from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    @staticmethod
    def wait_for_element_to_be_visible(wait, locator):
        return wait.until(
            EC.visibility_of_element_located(locator),
            message='Search input not shown'
        )

    @staticmethod
    def wait_for_element_to_be_clickable(wait, locator):
        return wait.until(
            EC.element_to_be_clickable(locator),
            message='Search icon not clickable'
        )