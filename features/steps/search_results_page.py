from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")

@when('Click on the first product')
def clock_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)

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


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        product_title = product.find_element(*PRODUCT_TITLE).text
        print(product_title)
        assert product_title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)
