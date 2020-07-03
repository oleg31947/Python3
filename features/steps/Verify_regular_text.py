from behave import given, when, then
from selenium.webdriver.common.by import By


RESULTS = (By.CSS_SELECTOR, "#wfm-pmd_deals_section div:last-child li")
# REGULAR = (By.CSS_SELECTOR, ".wfm-sales-item-card__regular-price")
# PRODUCT_NAME = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")

@given("Open Amazon 'wholefoodsdeals'")
def open_wholefoodsdeals(context):
    context.driver.get("https://www.amazon.com/wholefoodsdeals")

@then("Each item has regular field and Product name")
def verify_regular_field(context):
    all_products = context.driver.find_elements(*RESULTS)
    for index in range(len(all_products)):
        if 'Hundreds more in store. Look for the yellow signs.' not in all_products[index]:
            assert "Regular" in all_products[index], f'we expected to have Regular price in the {all_products[index]}'

