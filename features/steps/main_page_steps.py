from behave import given, when, then


@given('Open Target.com')
def open_target_site(context):
    context.app.main_page.open_main_page()


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)
