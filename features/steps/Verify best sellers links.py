from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BUTTON = (By.XPATH, ".//div[@id='nav-xshop']/*[text()='Best Sellers']")
BLOC_LINKS = (By.CSS_SELECTOR, "div#zg_tabs li")
HEADERS = (By.CSS_SELECTOR, "div#zg_tabs li")


@when("Press on the {name_button} button")
def click(context, name_button):
    context.driver.find_element(*BUTTON)


@then("Verify Best sellers and others links")
# def verify_links(context):
#     expected_list_of_links = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']
#     bloc_of_links = context.driver.find_elements(*BLOC_LINKS)
#     for item in range(len(bloc_of_links)):
#         k = bloc_of_links[item].click().text
#         assert k in expected_list_of_links

# whe best way

# def verify_links(context):
#     bloc_of_links = context.driver.find_elements(*BLOC_LINKS)
#     for item in bloc_of_links:
#         link_text = item.click().text
#         print(link_text)
#
#         expected_list_of_links = context.driver.find_elements(*HEADERS)
#         print(expected_list_of_links)
#         assert expected_list_of_links in link_text, f'we expected {expected_list_of_links} but we got {link_text}'


# by Lana way

def verify_links(context):
    bloc_of_links = context.driver.find_elements(*BLOC_LINKS)
    for item in range(len(bloc_of_links)):
        link_to_click = context.driver.find_elements(*BLOC_LINKS)[item]
        link_text = link_to_click.text
        print(link_text)

        link_to_click.click()
        click()
        expected_list_of_links = context.driver.find_elements(*HEADERS)
        print(expected_list_of_links)
        assert expected_list_of_links in link_text, f'we expected {expected_list_of_links} but we got {link_text}'



