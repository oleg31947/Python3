from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page



class TopNavMenu(Page):
    ORDERS = (By.CSS_SELECTOR, "a#nav-orders")
    SHOPPING_CARD = (By.CSS_SELECTOR, "#nav-cart-count.nav-cart-count.nav-cart-0")

    def click_order_link(self):
        self.click(*self.ORDERS)


    def click_shopping_icon(self):
        self.click(*self.SHOPPING_CARD)

