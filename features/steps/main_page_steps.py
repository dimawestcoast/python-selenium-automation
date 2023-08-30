from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
ORDERS_BUTTON = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
SIGNIN_BTN = (By.CSS_SELECTOR, 'nav-signin-tooltip .nav-action-signin-button')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(2)
    context.driver.refresh()


@when('Search for {product}')
def search_on_amazon(context, product):
    context.app.header.search_product(product)
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BUTTON).click()


@when('User clicks on returns and orders')
def click_on_returns_orders(context):
    context.app.header.click_on_returns_orders()


@when('User clicks on bestsellers page')
def click_on_bestsellers(context):
    context.driver.find_element(By.CSS_SELECTOR, '[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]').click()


@when('Click on button from SignIn popup')
def click_signin_popup(context):
    context.app.header.click_signin_from_popup()


@when('Wait for 3 sec')
def wait_sec(context):
    sleep(3)


@then('Verify Sign In is clickable')
def verify_signin_btn_clickable(context):
    context.header.verify_signin_btn_clickable()


@then('Verify Sign In disappears')
def verify_signin_btn_disappears(context):
    context.app.header.verify_signin_btn_disappears()


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


@then('Verify there are 5 links on the page')
def verify_bestseller_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='nav-tab'] a")
    print(f'Total links {len(links)}')
    assert len(links) == 5, f'expected {5} but got {len(links)}'


