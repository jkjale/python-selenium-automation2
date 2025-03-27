from behave import given, when, then


@then('Click Sign In button')
def click_sign_in_btn(context):
    context.app.sign_in_page.click_sign_in_btn()


@then('Input username and password on Sign In page')
def input_username_and_password(context):
    context.app.sign_in_page.verify_username_field()
    context.app.sign_in_page.verify_password_field()
    context.app.sign_in_page.input_username_and_password()


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_url()
    context.app.sign_in_page.verify_page_header()
    context.app.sign_in_page.verify_username_field()
    context.app.sign_in_page.verify_password_field()


@then('Verify user is logged in and redirected to home page')
def verify_user_is_logged_in(context):
    context.app.sign_in_page.verify_user_is_logged_in()
