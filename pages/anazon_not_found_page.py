from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class NotFoundPage(Page):
    DOG_IMG = (By.CSS.SELECTOR, 'img#d')

    def store_original_window(self):
        return self.get_current_window()

    def click_dog_image(self):
        self.click(*DOG_IMG)