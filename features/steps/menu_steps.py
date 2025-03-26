from behave import given, when, then


@when('Click on "Add to cart" button in side navigation menu')
def click_addToCart_btn_in_nav_menu(context):
    context.app.menu.click_addToCart_btn_in_nav_menu()


@when('Click on "View cart & check out" button in side navigation menu')
def click_viewCartAndCheckOut_btn_in_nav_menu(context):
    context.app.menu.click_viewCartAndCheckOut_btn_in_nav_menu()


@then('From side navigation menu, click Sign In')
def click_sign_in(context):
    context.app.menu.click_sign_in()


@then('Side navigation menu is shown')
def verify_side_nav_menu(context):
    context.app.menu.verify_side_nav_menu()
