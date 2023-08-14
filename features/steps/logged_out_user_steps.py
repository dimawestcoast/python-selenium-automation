from behave import given, when, then
from selenium.webdriver.common.by import By


# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')


@when('User clicks on returns and orders')
def click_on_returns_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify user see sign in option')
def verify_signin_results(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1[class='a-spacing-small']").text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@given("Open Amazon")
def step_impl(context):
    context.driver.get("https://www.amazon.com/")