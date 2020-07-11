from behave import given, when, then
from selenium.webdriver.common.by import By

MORE_SOLUSHEN_FILD = (By.ID, "helpsearch")
GO = (By.XPATH, "//input[@class='a-button-input']")
HEADER = (By.XPATH, "//a[@class='a-link-normal'and contains(text(),'Cancel Items or Orders')]")

@given("Open Amazon Help page")
def open_amazon(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")

@when("Use Find more solutions field and search for {search_word}")
def search_cancel(context, search_word):
    search = context.driver.find_element(*MORE_SOLUSHEN_FILD)
    search.clear()
    search.send_keys(search_word)


@when("Click Go")
def click(context):
    context.driver.find_element(*GO).click()


@then("Check that {necessary} text is present")
def text_present(context, necessary):
    text = context.driver.find_element(*HEADER).text
    assert necessary == text, f'We expect {necessary} but got {text}'
