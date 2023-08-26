from behave import given, when, then
from selenium.webdriver.common.by import By


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Camel', 'Charcoal Marl', 'Forest Green',
                       'Light Grey', 'Navy', 'Off-white']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:7]: #  colors[:3]: first 3 elements only
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        # print(current_color)

        actual_colors.append(current_color)

    # print(actual_colors)
    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

