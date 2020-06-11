from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


SHOPPING_CARD = (By.CSS_SELECTOR, "#nav-cart-count.nav-cart-count.nav-cart-0")

EMPTY_CARD = (By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty")

SEARCH_FIELD = (By.CSS_SELECTOR, "#twotabsearchtextbox")

SEARCH_ICON =(By.CSS_SELECTOR, "input[type='submit'].nav-input")

# SPORT_SHOES = (By.CSS_SELECTOR, "[href*='Carhartt-Mens-Odessa-Cotton-Sandstone'] .a-price ")

SPORT_SHOES = (By.CSS_SELECTOR, ".a-price")

ADD_TO_CARD = (By.CSS_SELECTOR, "#add-to-cart-button")

QUANTITY = (By.CSS_SELECTOR, "#nav-cart-count")





@given("Open Amazon page")
def open_amazon(context):

    context.driver.get("https://www.amazon.com/")

    sleep(3)


@when("Clicks on the shopping cart icon")
def click_shopping_icon(context):

    context.driver.find_element(*SHOPPING_CARD).click()

    sleep(3)

@when("Search {item}")
def search_item(context, item):

    e = context.driver.find_element(*SEARCH_FIELD)

    e.clear()

    e.send_keys(item)

    sleep(1)

    context.driver.find_element(*SEARCH_ICON).click()

    sleep(3)




@when("Click on {item}")
def cleck_item(context, item):

    context.driver.find_element(*SPORT_SHOES).click()

    sleep(3)


@when("Add the item to the shopping card")
def add_item_in_card(context):

    context.driver.find_element(*ADD_TO_CARD).click()

    sleep(3)


@then("Verify {quantity} items")
def verify_quantity(context, quantity):
    actual_text = context.driver.find_element(*QUANTITY).text

    print(actual_text)

    assert quantity in actual_text, f'We expected {quantity}, but we got {actual_text}'


@then("Verifies that {text}")
def verify_text(context, text):

    actual_text = context.driver.find_element(*EMPTY_CARD).text

    sleep(3)

    print(actual_text)

    assert text == actual_text, f'We expected {text}, but we got {actual_text}'
