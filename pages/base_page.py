import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_element(self,locators):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(locators))

    def wait_for_clickable_element_for_home_page(self,locators):
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(locators))

    def click_button_order(self):
        self.wait_for_load_element(BasePageLocators.BUTTON_ORDER)
        self.driver.find_element(*BasePageLocators.BUTTON_ORDER).click()
        self.wait_for_load_element(BasePageLocators.FIELD_NAME)

    def switch_to_new_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def assert_current_url(self, url):
        WebDriverWait(self.driver,5).until(expected_conditions.url_to_be(url))
        assert self.driver.current_url == url

    def find_elements(self,locators):
        return self.driver.find_element(*locators)

    def execute_scripts(self,element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)