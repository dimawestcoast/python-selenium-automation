from behave import given, when, then

@then('Verify user see sign in option')
def verify_signin_results(context):
    context.app.signin_page.verify_signin_results()

@given("Open Amazon")
def step_impl(context):
    context.driver.get("https://www.amazon.com/")

@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)

@then('Verify sign in page opened')
def verify_signin_opened(context):
    context.app.signin_page.verify_signin_opened()