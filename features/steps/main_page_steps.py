from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.ID, "search")
SEARCH_SUBMIT = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@given('Open Target.com')
def open_target_site(context):
    context.driver.get('https://www.target.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(SEARCH_INPUT)
    )
    search.clear()
    search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    search_icon = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(SEARCH_SUBMIT)
    )
    search_icon.click()
