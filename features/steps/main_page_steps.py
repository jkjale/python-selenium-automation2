from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.ID, "search")
SEARCH_SUBMIT = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@given('Open Target.com')
def open_target_site(context):
    context.driver.get('https://www.target.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search_input = context.driver.wait.until(
        EC.visibility_of_element_located(SEARCH_INPUT),
        message='Search input not shown'
    )
    search_input.clear()
    search_input.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SEARCH_SUBMIT),
        message='Search icon not clickable'
    ).click()
