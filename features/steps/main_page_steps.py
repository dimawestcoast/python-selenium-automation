from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
ORDERS_BUTTON = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_on_amazon(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BUTTON).click()

@when('User clicks on returns and orders')
def click_on_returns_orders(context):
    context.driver.find_element(*ORDERS_BUTTON).click()


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    print(f'Total links {len(links)}')
    assert len(links) == expected_amount, f'expected {expected_amount} but got {len(links)}'


@then('Verify many link are shown in the footer')
def verify_many_links(context):
    # context.driver.find_element(*FOOTER_LINKS) # for a single element
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) > 1 #for multipe elements