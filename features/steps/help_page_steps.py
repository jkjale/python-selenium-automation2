from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TARGET_HELP_HEADER = (By.XPATH, "//*[contains(text(), 'Target Help')]")
SEARCH_INPUT = (By.CSS_SELECTOR, ".social-column > div > input:nth-child(1)")
SEARCH_ICON = (By.CSS_SELECTOR, ".social-column > div > input:nth-child(2)")
WHAT_SECTION = (By.CSS_SELECTOR, ".section > div:nth-child(3)")
CONTACT_LINKS = (By.CSS_SELECTOR, ".section > div:nth-child(4)")
BROWSE_ALL_HEADER = (By.XPATH, "//*[text()='Browse all Help pages']")


@given('Open help.target.com/help')
def open_help_page(context):
    context.driver.get('https://help.target.com/help')


@then('"Target Help" header is shown')
def verify_target_help_header(context):
    target_help_header = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(TARGET_HELP_HEADER)
    )
    assert target_help_header.text.strip().title() == 'Target Help', 'Header should be shown'


@then('Search input is shown')
def verify_search_input_is_shown(context):
    context.driver.find_element(*SEARCH_INPUT)


@then('Search icon is shown')
def verify_search_icon_is_shown(context):
    context.driver.find_element(*SEARCH_ICON)


@then('"What would you like to do" section is shown')
def verify_section_is_shown(context):
    context.driver.find_element(*WHAT_SECTION)


@then('"contact us" and "product recalls" section is shown')
def verify_contactUsAndProductRecalls_links_are_shown(context):
    context.driver.find_element(*CONTACT_LINKS)


@then('"Browse all Help pages" header is shown')
def verify_browseAllHelpPages_header(context):
    browse_all_header = context.driver.find_element(*BROWSE_ALL_HEADER)
    assert browse_all_header.text.strip().lower() == 'browse all help pages', 'Header should be shown'
