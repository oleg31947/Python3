from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")
RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@given("Open Amazon {address} page")
def open_amazon_page(context,address ):
    context.app.product.open_amazon_page(address)


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click to search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@when("Select {title} department")
def select_department(contest, title):
    contest.app.top_nav_menu.select_department(title)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)


@then('First result contains {search_word}')
def verify_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)


@then("{selected_dep} department was selected")
def verify_selected_department(context, selected_dep):
    context.app.top_nav_menu.verify_selected_department(selected_dep)