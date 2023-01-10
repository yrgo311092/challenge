from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BasePage:
    def __init__(self, driver: Remote):
        self.driver = driver

    def wait_element_visible(self, loc, elem) -> WebElement:
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((loc, elem)))

    def wait_element_by_located(self, loc, elem) -> WebElement:
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((loc, elem)))

    def wait_element_is_clickable(self, loc, elem) -> WebElement:
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((loc, elem)))

    def wait_element_is_invisibility(self, loc, elem) -> WebElement:
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((loc, elem)))
