import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    def wait_for_clickable_element_for_home_page(self,locators):
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(locators))

    @allure.step('Кликаем по стрелочке с вопросами')
    def click_arrow_for_questions_about_great(self,locators):
        element = self.driver.find_element(*locators)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_load_element(locators)
        self.wait_for_clickable_element_for_home_page(locators)
        self.driver.find_element(*locators).click()
    @allure.step('Получаем текст соответсвующего вопроса')
    def get_text_questions_about_great(self, locators):
        return self.driver.find_element(*locators).text

    def check_text_questions_about_great(self,text_for_front, locators_arrow, locators_text):
        self.wait_for_load_element(locators_arrow)
        self.click_arrow_for_questions_about_great(locators_arrow)
        self.wait_for_load_element(locators_text)
        with allure.step('Сравниваем текст'):
            assert text_for_front == self.get_text_questions_about_great(locators_text)

    @allure.step('Нажатие на логотип "Самоката"')
    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.wait_for_load_element(MainPageLocators.LOGO_YANDEX)
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()