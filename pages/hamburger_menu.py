from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class HamburgerMenu(Page):
    HAMBURGER = (By.CSS_SELECTOR, "a#nav-hamburger-menu i")
    # AMAZON_MUSIC = (By.XPATH, ".//div[@id='hmenu-content']// div[text()='Amazon Music']")
    AMAZON_MUSIC = (By.XPATH, ".//ul[@class='hmenu hmenu-visible']//*[text()='Amazon Music']")
    MENU_ITEMS = (By.CSS_SELECTOR, "ul.hmenu.hmenu-visible a:not(.hmenu-back-button)")

    def click_hamburger_menu(self):
        self.click(*self.HAMBURGER)

    def click_to_item(self):
        e = self.driver.wait.until(EC.element_to_be_clickable(self.AMAZON_MUSIC))
        e.click()
        # self.driver.wait.until(EC.presence_of_element_located(self.AMAZON_MUSIC)).click()
        # sleep(3)

    def verify_menu_items(self, quantity: int):
        self.driver.wait.until(EC.visibility_of_any_elements_located(self.MENU_ITEMS))
        # actual_items = self.driver.find_elements(*self.MENU_ITEMS)
        actual_items = len(self.driver.find_elements(*self.MENU_ITEMS))
        quantity = int(quantity)
        print(type(actual_items))
        print((type(quantity)))

        assert quantity == actual_items, f'we expect {quantity}, but we got {actual_items}'


