from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

COLOR_OPTION = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] > div:nth-child(2) > ul > li > a")
COLOR_LABEL = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] > div:nth-child(1)")


@given('Open Target product {product_id} page')
def open_target_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(7)


@then('Click and verify colors starting at color index {color_ind} and labels list index {labels_list_ind}')
def click_on_color_options(context, color_ind, labels_list_ind):
    colors = context.driver.find_elements(*COLOR_OPTION)
    first_ind = int(color_ind)
    labels_ind = int(labels_list_ind)
    for color in colors[first_ind:first_ind + 4]:
        color.click()
        color_selection = color.get_attribute('value').strip()
        color_label = context.driver.find_elements(*COLOR_LABEL)[labels_ind].get_attribute('aria-label')
        assert color_selection == color_label[6:], 'Not showing the correct color label!!'
