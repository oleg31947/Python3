from behave import given, when, then
from selenium.webdriver.common.by import By


@when("Hover over to New Arrivals button")
def hover_over_new_arrivals(context):
    context.app.product.hover_over_new_arrivals()

@then("Verify selection tooltip is shown")
def verify_tooltip(context):
    context.app.product.verify_tooltip()