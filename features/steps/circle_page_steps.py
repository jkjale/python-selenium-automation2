from selenium.webdriver.common.by import By
from behave import given, when, then

BENEFIT_CELL = (By.CSS_SELECTOR, ".cell-item-content")


@given('Open Target.com/circle')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('At least {count} benefit cells are shown')
def verify_number_of_cells_shown(context, count):
    benefit_cells = context.driver.find_elements(*BENEFIT_CELL)
    assert len(benefit_cells) >= int(count), f'Did not find at least {count} benefit cells'
