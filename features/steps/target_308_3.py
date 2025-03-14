from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Click the "Sign In" link on the homepage')
def click_sign_in_link(context):
    sign_in_link = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='@web/AccountLink']"))
    )
    sign_in_link.click()


@when('Click the "Sign In" button from the right side navigation menu')
def click_sign_in_button(context):
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='accountNav-signIn']"))
    )
    sign_in_button.click()


@then('"Sign In" form is shown')
def verify_sign_in_form(context):
    sign_in_form = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#__next > div form"))
    )
    assert sign_in_form.is_displayed(), "Sign In form is not visible!!"
    username_input = context.driver.find_element(By.CSS_SELECTOR, "#username")
    assert username_input.is_enabled(), "Username input field is not enabled!!"
