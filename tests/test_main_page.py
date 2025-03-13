from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
import allure
from urls.base_page_urls import BasePageUrls
from data.data import Data
import pytest

class TestMainPage:

    @pytest.mark.parametrize("data", [
        (
                {'text_for_front': Data.TEXT_HOW_MUCH, 'locators_arrow': MainPageLocators.ARROW_HOW_MUCH, 'locators_text': MainPageLocators.TEXT_ARROW_HOW_MUCH}
        ),
        (
                {'text_for_front': Data.TEXT_WANT_SOME_SCOOTER, 'locators_arrow': MainPageLocators.ARROW_WANT_SOME_SCOOTER, 'locators_text': MainPageLocators.TEXT_ARROW_WANT_SOME_SCOOTER}
        ),
        (
                {'text_for_front': Data.TEXT_HOW_IS_RENTAL_TIME_CALCULATED,
                 'locators_arrow': MainPageLocators.ARROW_HOW_IS_RENTAL_TIME_CALCULATED,
                 'locators_text': MainPageLocators.TEXT_ARROW_HOW_IS_RENTAL_TIME_CALCULATED}
        ),
        (
                {'text_for_front': Data.TEXT_ODER_SCOOTER_TODAY,
                 'locators_arrow': MainPageLocators.ARROW_ORDER_SCOOTER_TODAY,
                 'locators_text': MainPageLocators.TEXT_ARROW_ORDER_SCOOTER_TODAY}
        ),
        (
                {'text_for_front': Data.TEXT_EXTEND_OR_RETURN_SCOOTER,
                 'locators_arrow': MainPageLocators.ARROW_EXTEND_OR_RETURN_SCOOTER,
                 'locators_text': MainPageLocators.TEXT_ARROW_EXTEND_OR_RETURN_SCOOTER}
        ),
        (
                {'text_for_front': Data.TEXT_CHARGER_WITH_SCOOTER,
                 'locators_arrow': MainPageLocators.ARROW_CHARGER_WITH_SCOOTER,
                 'locators_text': MainPageLocators.TEXT_ARROW_CHARGER_WITH_SCOOTER}
        ),
        (
                {'text_for_front': Data.TEXT_CANCEL_AN_ORDER,
                 'locators_arrow': MainPageLocators.ARROW_CANCEL_AN_ORDER,
                 'locators_text': MainPageLocators.TEXT_ARROW_CANCEL_AN_ORDER}
        ),
        (
                {'text_for_front': Data.TEXT_LIVE_OUTSIDE_MKAD,
                 'locators_arrow': MainPageLocators.ARROW_LIVE_OUTSIDE_MKAD,
                 'locators_text':  MainPageLocators.TEXT_ARROW_LIVE_OUTSIDE_MKAD}
        )
    ])
    @allure.title('Проверка текста по нажатию стрелочку')
    def test_chech_text_for_questions_about(self, driver,data):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.check_text_questions_about_great(data['text_for_front'],data['locators_arrow'],data['locators_text'])

    @allure.title('Проверка перехода на главную страницу Самоката')
    def test_check_go_home(self,driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_button_order()
        main_page.click_scooter_logo()
        main_page.assert_current_url(BasePageUrls.URL_MAIN_PAGE)


    @allure.title('Проверка перехода с главной страницы на главную страницу Дзена')
    def test_passage_to_dzen(self,driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        main_page.assert_current_url(BasePageUrls.URL_DZEN)