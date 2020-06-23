from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

SELECTED_COLORS = (By.CSS_SELECTOR, "div#variation_color_name span.selection")
COLORS_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")


@given("Open Amazon product {page}")
def open_amazon_product(context, page):
    context.driver.get(f'https://www.amazon.com/gp/product/{page}/')

@then("Verify user can select through colors")
def verify_jeans_colors(context):

    expected_colors = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash',
                       'Light Wash', 'Medium Wash', 'Rinse', 'Vintage Light Wash']
    colors_options = context.driver.find_elements(*COLORS_OPTIONS)
    print(colors_options)

    for x in range(len(colors_options)):
        colors_options[x].click()
        selected_colors_text = context.driver.find_element(*SELECTED_COLORS).text

    # for color in colors_options:
    #     color.click()

        assert selected_colors_text == expected_colors[x], f'we expected get {expected_colors[x]}, but we got {selected_colors_text}'
        # assert selected_colors_text == expected_colors[colors_options.index(color)], f'we expected get {selected_colors_text}, but we got {expected_colors[colors_options.index(color)]}'