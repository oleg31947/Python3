from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select



class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'
        self.driver.implicitly_wait(5)
        self.waite = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)


    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def verify_text(self, expected_text: str, *locator):
        # actual_text = self.driver.find_element(*locator).text
        actual_text = self.driver.wait.until(EC.presence_of_element_located(locator)).text
        print(f'actual {actual_text}')
        print(type(actual_text))
        print(f'expected {expected_text}')
        print(type(expected_text))
        assert expected_text == actual_text, f'Expected text{expected_text}, but we got {actual_text}'

    def wait_for_element_appears(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

