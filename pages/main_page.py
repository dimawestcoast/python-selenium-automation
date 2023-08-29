from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

ORDERS_BUTTON = (By.ID, 'nav-orders')

class MainPage(Page):

    def open_main(self):
        self.driver.get('https://www.amazon.com/')
        sleep(2)
        self.driver.refresh()

