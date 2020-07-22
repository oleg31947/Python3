from pages.base_page import Page
from pages.top_nav_menu import TopNavMenu
from pages.click_result import ClickResult
from pages.hamburger_menu import HamburgerMenu
from pages.product_page import Products

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)

        self.top_nav_menu = TopNavMenu(self.driver)
        self.click_result = ClickResult(self.driver)
        self.hamburger = HamburgerMenu(self.driver)
        self.product = Products(self.driver)


