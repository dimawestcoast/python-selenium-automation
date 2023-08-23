from behave import given, when, then
from selenium.webdriver.common.by import By


@when('Click on the first product')
def clock_first_product(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-cel-widget="MAIN-SEARCH_RESULTS-3"] span.a-price-whole').click()

@when('Click on Add to cart button')
def add_to_cart_button(context):
    context.driver.find_element(By. ID, 'add-to-cart-button').click()
    context.driver.find_element(By. ID, 'attachSiNoCoverage').click()

# @when('Open cart page')
# def open_cart_page(context):
#     context.driver.find_element(By. ID, 'nav-cart-count-container').click()

@then('Verify cart has 1 item(s)')
def verify_cart_full(context):
    expected_results = 'Added to Cart'
    act_res = context.driver.find_element(By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base.sw-atc-text').text
    assert expected_results == act_res, f'Error, expected {expected_results} did not match actual {act_res}'