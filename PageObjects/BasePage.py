from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def is_displayed(self, by_locator):
        value = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(value)

    def sendkeys(self, by_locator, value):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        element.send_keys(value)
