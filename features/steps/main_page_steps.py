from behave import given, when, then


@given('Open Target.com')
def open_target_site(context):
    context.app.main_page.open_main_page()


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)


@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()
