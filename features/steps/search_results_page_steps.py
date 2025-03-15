from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BUTTON_IN_PRODUCT = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
ADD_TO_CART_BUTTON_IN_NAV = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
PRODUCTS_LIST = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
RESULTS_CATEGORY_NAME = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] > span")
RIGHTSIDE_NAV_PANEL = (By.XPATH, "//div[@class='ModalDrawer']/div[1]/div[1]")
VIEWCART_AND_CHECKOUT_BUTTON = (By.XPATH, "//div[@data-test='content-wrapper']/div[3]/a")


@when('Click on "Add to cart" button on a product')
def click_on_addToCart_button_on_product(context):
    products_list = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_all_elements_located(PRODUCTS_LIST)
    )
    first_product = products_list[0]
    add_to_cart_button_in_product = first_product.find_element(*ADD_TO_CART_BUTTON_IN_PRODUCT)
    add_to_cart_button_in_product.click()


@when('Click on "Add to cart" button in the navigation panel')
def click_on_addToCart_button_in_navPanel(context):
    add_to_cart_button_in_nav = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(ADD_TO_CART_BUTTON_IN_NAV)
    )
    add_to_cart_button_in_nav.click()


@when('Click on the "View cart & check out" button in navigation panel')
def click_on_viewCartAndCheckOut_button_in_navPanel(context):
    viewcart_and_checkout_button = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(VIEWCART_AND_CHECKOUT_BUTTON)
    )
    viewcart_and_checkout_button.click()


@then('Product results for {search_word} are shown')
def verify_found_results(context, search_word):
    results_category_name = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(RESULTS_CATEGORY_NAME)
    )
    assert search_word.lower() in results_category_name.text.lower(), 'Results category name not found'
    assert search_word.lower() in context.driver.current_url.lower(), f'Expected query not in {context.driver.current_url.lower()}'


@then('Right-side navigation panel with "Add to cart" button is shown')
def verify_navPanel_with_addToCart_button(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(RIGHTSIDE_NAV_PANEL)
    )
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(ADD_TO_CART_BUTTON_IN_NAV)
    )
