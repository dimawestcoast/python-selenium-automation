from behave import given, when, then
from selenium.webdriver.common.by import By

@when('Clicking on cart icon')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '.nav-cart-icon.nav-sprite').click()


@then('Verify cart is empty')
def verify_cart_empty(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty").text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
