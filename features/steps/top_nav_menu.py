from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


@when("Press on Amazon Orders link")
def click_orders_link(context):
    context.app.top_nav_menu.click_order_link()


@when("Clicks on the shopping cart icon")
def click_shopping_icon(context):
    context.app.top_nav_menu.click_shopping_icon()


@when("Click to hamburger menu")
def click_hamburger_menu(context):
    context.app.hamburger.click_hamburger_menu()


@when("Click to {item}")
def click_to_item(context, item):
    context.app.hamburger.click_to_item()


@then("Verify 'Sign In' page is opened")
def verify_sign_in(context):
    context.app.click_result.verify_sign_in()


@then("User can verify {text}")
def verify_empty_card(context, text):
    context.app.click_result.verify_text(text)


@then("{quantity} menu items are present")
def verify_menu_items(context, quantity):
    context.app.hamburger.verify_menu_items(quantity)
