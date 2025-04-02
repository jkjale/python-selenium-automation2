from behave import given, when, then


@given('Open help.target.com/help')
def open_help_page(context):
    context.app.base_page.open_url('https://help.target.com/help')


@then('"Target Help" header is shown')
def verify_target_help_header(context):
    context.app.help_page.verify_target_help_header()


@then('Search input is shown')
def verify_search_input(context):
    context.app.help_page.verify_search_input()


@then('Search icon is shown')
def verify_search_icon_is_shown(context):
    context.app.help_page.verify_search_icon()


@then('"What would you like to do" section is shown')
def verify_ask_section(context):
    context.app.help_page.verify_ask_section()


@then('"contact us" and "product recalls" section is shown')
def verify_contact_us_links(context):
    context.app.help_page.verify_contact_us_links()


@then('"Browse all Help pages" header is shown')
def verify_browse_all_header(context):
    context.app.help_page.verify_browse_all_header()
