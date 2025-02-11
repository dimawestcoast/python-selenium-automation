from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage
from pages.not_found_page import NotFoundPage
from pages.blog_page import BlogPage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)
        self.not_found_page = NotFoundPage
        self.blog_page = BlogPage

