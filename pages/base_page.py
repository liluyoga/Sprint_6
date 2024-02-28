from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_waiting(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_and_click_on_element(self, locator):
        element = self.find_element_with_waiting(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    def click_on_element(self, locator):
        element = self.find_element_with_waiting(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_waiting(locator)
        return element.text

    def input_value_to_field(self, locator, value):
        element = self.find_element_with_waiting(locator)
        element.send_keys(value)

    @staticmethod
    def format_locator(locator, num):
        method, value = locator
        value = value.format(num)
        locator = (method, value)
        return locator

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def get_current_url(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        current_url = self.driver.current_url
        return current_url

    def accept_cookies(self, locator):
        if locator:
            self.click_on_element(locator)
