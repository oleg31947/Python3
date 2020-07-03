from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BUTTON = (By.XPATH, ".//div[@id='nav-xshop']/*[text()='Best Sellers']")
BLOC_LINKS = (By.CSS_SELECTOR, "div#zg_tabs li")


@when("Press on the {name_button} button")
def click(context, name_button):
    context.driver.find_element(*BUTTON)


@then("Verify Best sellers and others links")
def verify_links(context):
    expected_list_of_links = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']
    bloc_of_links = context.driver.find_elements(*BLOC_LINKS)
    for item in range(len(bloc_of_links)):
        k = bloc_of_links[item].click().text
        assert k in expected_list_of_links
