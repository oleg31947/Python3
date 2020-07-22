from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pages.base_page import Page


class Products(Page):
    NEW_ARRIVALS = (By.XPATH, ".//div[@id='nav-subnav']//*[contains(text(),'New Arrivals')]")
    TOOLTIP_NEW_ARRIVALS = (By.ID, "nav-flyout-aj:https://images-na.ssl-images-amazon.com/images/G/01/softlines/megamenu/prod/megamenu-contents_en_US._TTH_.json:subnav-sl-megamenu-8:0")

    def open_amazon_page(self, address):
        self.open_page(address)

    def hover_over_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        self.action.move_to_element(new_arrivals).perform()
        # self.action.perform()   (same)

    def verify_tooltip(self):
        self.wait_for_element_appears(*self.TOOLTIP_NEW_ARRIVALS)