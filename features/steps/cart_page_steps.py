from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CART_ITEM = (By.CSS_SELECTOR, "[data-test='cart-item-groups']")
CART_ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='cartItem-price']")
SUBTOTAL = (By.CSS_SELECTOR, "[data-test='cart-summary-subTotal'] > div:nth-child(2) > p")


@then('Cart page is displayed with the added item and correct subtotal')
def verify_cart_page(context):
    items = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_all_elements_located(CART_ITEM)
    )
    assert len(items) == 1, 'Item not found in cart'
    first_item = items[0]
    first_item_price = first_item.find_element(*CART_ITEM_PRICE).text
    subtotal = context.driver.find_element(*SUBTOTAL).text
    assert first_item_price.strip() == subtotal.strip(), 'Subtotal is incorrect'
