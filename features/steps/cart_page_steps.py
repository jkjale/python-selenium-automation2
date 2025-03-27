from behave import given, when, then


@then('Cart page is displayed with the added item and correct subtotal')
def verify_cart_content(context):
    context.app.cart_page.verify_cart_content()


@then('Verify "Your cart is empty" message is shown')
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_empty_cart_msg()
