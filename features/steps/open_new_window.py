from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEALS = (By.CSS_SELECTOR, "div#desktop-btf-grid-1 a.a-link-normal.see-more.truncate-1line")


@when("Store original windows")
def store_windows(context):
    context.original_windows = context.driver.window_handles
    original_window = context.driver.current_window_handle
    print(f'Oroginal window {original_window}')


@when("Click to open See more from Gift finder")
def click(context):
    new_window = context.driver.find_element(*DEALS).click()
    context.driver.wait.until(EC.new_window_is_opened)


@when("Switch to the newly opened window")
def switch_windows(context):
    new_windows = context.driver.window_handles
    print(f'New windows {new_windows}')

    for old_window in context.original_windows:
        new_windows.remove(old_window)
    print(f' after loop {new_windows}')
    context.driver.switch_to_window(new_windows[0])






