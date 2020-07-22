from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class TopNavMenu(Page):
    ORDERS = (By.CSS_SELECTOR, "a#nav-orders")
    SHOPPING_CARD = (By.CSS_SELECTOR, "#nav-cart-count.nav-cart-count.nav-cart-0")
    SELECT_DEPARTMENT = (By.ID, "searchDropdownBox")
    # (same) SELECT_DEPARTMENT = (By.CSS_SELECTOR, "select.nav-search-dropdown")
    # BABY = (By.CSS_SELECTOR, "div.a-section.a-spacing-small.a-spacing-top-small a.a-link-normal.a-text-normal")
    BABY = (By.CSS_SELECTOR, "#nav-subnav .nav-a.nav-b")

    def click_order_link(self):
        self.click(*self.ORDERS)

    def click_shopping_icon(self):
        self.click(*self.SHOPPING_CARD)

    def select_department(self, title):
        department_selection_element = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(department_selection_element)
        # (the same) select = Select(self.find_element(*self.SELECT_DEPARTMENT)
        select.select_by_value(f'search-alias={title}')
        # select_by_name('name'))
        # select_by_index('index'))
        # select_by_text('text'))

    def verify_selected_department(self, selected_dep):
        self.verify_text(selected_dep, *self.BABY)
