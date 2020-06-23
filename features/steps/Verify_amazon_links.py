from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given("Open Amazon best sellers page")
def open_best_page(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")

@then("Verify 5 Amazon links")
def find_links_bloc(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "div#zg_tabs li")
    print(len(links))
    print(type(len(links)))

    if int(len(links)) == 5:
        print("Test passed well")
    else:
        print("Test failed")