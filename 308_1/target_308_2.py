from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open Target.com')
def open_target_site(context):
    context.driver.get('https://www.target.com/')


@when('Click on the Cart icon')
def click_cart_icon(context):
    cart_icon = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='@web/CartIcon']"))
    )
    cart_icon.click()


@then('"Your cart is empty" message is shown')
def verify_empty_cart_message(context):
    empty_cart_message_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] > h1"))
    )
    empty_cart_message = empty_cart_message_element.text
    assert empty_cart_message.strip().capitalize() == 'Your cart is empty', 'Wrong cart message!!'
    context.driver.quit()
