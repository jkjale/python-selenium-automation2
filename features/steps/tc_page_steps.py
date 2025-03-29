from behave import given, when, then


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window:', context.original_window)


@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_target_terms_and_conditions_link()


@when('Switch to the newly opened window')
def switch_to_window(context):
    context.app.base_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tc_page(context):
    context.app.tc_page.verify_tc_page()


@then('User can close new window and switch back to original')
def close_page(context):
    context.app.base_page.close()
    print('Switching to original', context.original_window)
    context.app.base_page.switch_to_window_by_id(context.original_window)
