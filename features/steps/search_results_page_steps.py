from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

ADD_TO_CART_BUTTON_IN_NAV = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
ADD_TO_CART_BUTTON_IN_PRODUCT = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
PRODUCT_CARD = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary'] > img")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='product-title'] > div")
PRODUCTS_LIST = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
RESULTS_CATEGORY_NAME = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] > span")
RIGHTSIDE_NAV_PANEL = (By.XPATH, "//div[@class='ModalDrawer']/div[1]/div[1]")
VIEWCART_AND_CHECKOUT_BUTTON = (By.XPATH, "//div[@data-test='content-wrapper']/div[3]/a")


@when('Click on "Add to cart" button on a product')
def click_on_addToCart_button_on_product(context):
    products_list = context.driver.wait.until(
        EC.visibility_of_all_elements_located(PRODUCTS_LIST),
        message='Product list is empty'
    )
    first_product = products_list[0]
    add_to_cart_button_in_product = first_product.find_element(*ADD_TO_CART_BUTTON_IN_PRODUCT)
    add_to_cart_button_in_product.click()


@when('Click on "Add to cart" button in the navigation panel')
def click_on_addToCart_button_in_navPanel(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BUTTON_IN_NAV),
        message='Navigation panel not shown'
    ).click()


@when('Click on the "View cart & check out" button in navigation panel')
def click_on_viewCartAndCheckOut_button_in_navPanel(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(VIEWCART_AND_CHECKOUT_BUTTON),
        message='"View cart & check out" button not clickable'
    ).click()


@then('Product results for {search_word} are shown')
def verify_found_results(context, search_word):
    results_category_name = context.driver.wait.until(
        EC.visibility_of_element_located(RESULTS_CATEGORY_NAME),
        message='Results category name not shown'
    )
    assert search_word.lower() in results_category_name.text.lower(), 'Results category name not found'
    assert search_word.lower() in context.driver.current_url.lower(), f'Expected query not in {context.driver.current_url.lower()}'


@then('Right-side navigation panel with "Add to cart" button is shown')
def verify_navPanel_with_addToCart_button(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(RIGHTSIDE_NAV_PANEL),
        message='Right-side navigation panel not shown'
    )
    context.driver.wait.until(
        EC.visibility_of_element_located(ADD_TO_CART_BUTTON_IN_NAV),
        message='"Add to cart" button not shown'
    )


@then("Each product's name and image are shown")
def verify_name_and_image_shown(context):
    product_cards = context.driver.wait.until(
        EC.visibility_of_all_elements_located(PRODUCT_CARD),
        message='Product card not shown'
    )
    for card in product_cards[:8]:
        name = card.find_element(*PRODUCT_NAME)
        image = card.find_element(*PRODUCT_IMAGE)
        name_title = ''.join(c for c in name.get_attribute('title').strip().lower() if c != ' ')
        name_text = ''.join(c for c in name.text.strip().lower() if c != ' ')
        image_alt = ''.join(c for c in image.get_attribute('alt').strip().lower() if c != ' ')
        assert name_title == name_text == image_alt, 'Product name and image title mismatch or missing'
