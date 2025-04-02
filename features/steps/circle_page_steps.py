from behave import given, when, then


@given('Open Target.com/circle')
def open_circle_page(context):
    context.app.base_page.open_url('https://www.target.com/circle')


@then('At least {count} benefit cells are shown')
def verify_number_of_cells_shown(context, count):
    context.app.circle_page.verify_number_of_cells_shown(count)
