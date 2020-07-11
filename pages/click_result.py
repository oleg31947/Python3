from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class ClickResult(Page):
    EMPTY_CARD = (By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty")

    # @then("Verify 'Sign In' page is opened")
    def verify_sign_in(self):
        assert "https://www.amazon.com/ap/signin" in self.driver.current_url

    # @then("User can verify {text}")
    def verify_text(self, text):
        actual_text = self.find_element(*self.EMPTY_CARD).text
        print(actual_text)
        assert text == actual_text, f'We expected {text}, but we got {actual_text}'
