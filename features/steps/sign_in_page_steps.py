from behave import given, when, then

@then('Verify user see sign in option')
def verify_signin_results(context):
    context.app.signin_page.verify_signin_results()

@given("Open Amazon")
def step_impl(context):
    context.driver.get("https://www.amazon.com/")