from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.CSS_SELECTOR, "h1[class='a-spacing-small']")

    def verify_signin_results(self):
        expected_result = 'Sign in'
        actual_result = self.driver.find_element(*self.SIGNIN_HEADER).text
        assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

