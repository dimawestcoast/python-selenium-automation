from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    ORDERS_BUTTON = (By.ID, 'nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    LANG_SELECTION = (By.CSS_SELECTOR, ".icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href="switch-lang=es_US"]')
    DEPT_SELECTION = (By. ID, 'searchDropdownBox')
    SUBHEADER_DEPT = (By.CSS_SELECTOR, "#nav-subnav[data-category='{SUB_STR}']")


    def get_subheader_dept_locator(self, dept):
        return [self.SUBHEADER_DEPT[0], self.SUBHEADER_DEPT[1].replace('{SUB_STR}', dept)]

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

    def hover_lang(self):
        actions = ActionChains(self.driver)
        lang = self.find_element(*self.LANG_SELECTIONS)
        actions.move_to_element(lang)
        actions.perform()
        from time import sleep
        sleep(3)

    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def verify_dept_selected(self):
        subheader_locator = self.get_subheader_dept_locator(dept)
        self.wait_for_element_appear(*subheader_locator)




