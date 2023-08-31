from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    ORDERS_BUTTON = (By.ID, 'nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

    def click_on_returns_orders(self):
        self.click(*self.ORDERS_BUTTON)

    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(self.SIGNIN_BTN)

    def verify_signin_btn_clickable(self):
        self.wait_for_element_clickable(self.SIGNIN_BTN)

    def verify_signin_btn_disappears(self):
        self.wait_for_element_disappear(self.SIGNIN_BTN)
