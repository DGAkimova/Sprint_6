import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем пока загрузиться элемент')
    def wait_for_load_element(self,locators):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(locators))

    @allure.step('Нажимаем на кнопку Заказать')
    def click_button_order(self):
        self.wait_for_load_element(MainPageLocators.BUTTON_ORDER)
        self.driver.find_element(*MainPageLocators.BUTTON_ORDER).click()
        self.wait_for_load_element(OrderPageLocators.FIELD_NAME)

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    @allure.step('Проверка адреса страницы')
    def assert_current_url(self, url):
        WebDriverWait(self.driver,5).until(expected_conditions.url_to_be(url))
        assert self.driver.current_url == url