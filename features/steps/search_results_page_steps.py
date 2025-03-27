from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

ADD_TO_CART_BTN_IN_PRODUCT = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
PRODUCT_CARD = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary'] > img")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='product-title'] > div")
PRODUCTS_LIST = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")


@when('Click on "Add to cart" button on the product')
def click_addToCart_btn_on_product(context):
    context.app.search_results_page.click_addToCart_btn_on_product()


@then('Verify search results shown for {search_word}')
def verify_search_results(context, search_word):
    context.app.search_results_page.verify_search_results(search_word)


@then('Verify {search_word} in URL')
def verify_search_url(context, search_word):
    context.app.search_results_page.verify_search_url(search_word)


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
