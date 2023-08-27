from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')

    def verify_search_results(self, expected_text):
        actual_text = self.find_element(*self.SEARCH_RESULT).text
        assert actual_text == expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'