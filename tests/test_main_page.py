from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
import allure
from urls.base_page_urls import BasePageUrls

class TestMainPage:
    TEXT_HOW_MUCH = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    TEXT_WANT_SOME_SCOOTER = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    TEXT_HOW_IS_RENTAL_TIME_CALCULATED = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    TEXT_ODER_SCOOTER_TODAY = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    TEXT_EXTEND_OR_RETURN_SCOOTER = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    TEXT_CHARGER_WITH_SCOOTER = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    TEXT_CANCEL_AN_ORDER = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    TEXT_LIVE_OUTSIDE_MKAD = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    @allure.title('Проверка текста по нажатию стрелочку «Сколько это стоит? И как оплатить?»')
    def test_chech_text_for_questions_about_great_how_much(self,driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.check_text_questions_about_great(self.TEXT_HOW_MUCH,MainPageLocators.ARROW_HOW_MUCH,MainPageLocators.TEXT_ARROW_HOW_MUCH)
    @allure.title('Проверка текста по нажатию стрелочку «Хочу сразу несколько самокатов! Так можно?»')
    def test_chech_text_for_questions_about_great_want_some_scooter(self,driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.check_text_questions_about_great(self.TEXT_WANT_SOME_SCOOTER,MainPageLocators.ARROW_WANT_SOME_SCOOTER,MainPageLocators.TEXT_ARROW_WANT_SOME_SCOOTER)

    @allure.title('Проверка текста по нажатию стрелочку «Как рассчитывается время аренды?»')
    def test_chech_text_for_questions_about_great_how_is_rental_time_calculated(self, driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.check_text_questions_about_great(self.TEXT_HOW_IS_RENTAL_TIME_CALCULATED,
                                                   MainPageLocators.ARROW_HOW_IS_RENTAL_TIME_CALCULATED,
                                                   MainPageLocators.TEXT_ARROW_HOW_IS_RENTAL_TIME_CALCULATED)

    @allure.title('Проверка текста по нажатию стрелочку «Можно ли заказать самокат прямо на сегодня?»')
    def test_chech_text_for_questions_about_great_order_scooter_today(self, driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.check_text_questions_about_great(self.TEXT_ODER_SCOOTER_TODAY,
                                                   MainPageLocators.ARROW_ORDER_SCOOTER_TODAY,
                                                   MainPageLocators.TEXT_ARROW_ORDER_SCOOTER_TODAY)

    @allure.title('Проверка текста по нажатию стрелочку «Можно ли продлить заказ или вернуть самокат раньше?»')
    def test_chech_text_for_questions_about_great_extend_or_return_scooter(self, driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.check_text_questions_about_great(self.TEXT_EXTEND_OR_RETURN_SCOOTER,
                                                   MainPageLocators.ARROW_EXTEND_OR_RETURN_SCOOTER,
                                                   MainPageLocators.TEXT_ARROW_EXTEND_OR_RETURN_SCOOTER)

    @allure.title('Проверка текста по нажатию стрелочку «Вы привозите зарядку вместе с самокатом?»')
    def test_chech_text_for_questions_about_great_charger_with_scooter(self, driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.check_text_questions_about_great(self.TEXT_CHARGER_WITH_SCOOTER,
                                                   MainPageLocators.ARROW_CHARGER_WITH_SCOOTER,
                                                   MainPageLocators.TEXT_ARROW_CHARGER_WITH_SCOOTER)

    @allure.title('Проверка текста по нажатию стрелочку «Можно ли отменить заказ?»')
    def test_chech_text_for_questions_about_great_cancel_an_order(self, driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.check_text_questions_about_great(self.TEXT_CANCEL_AN_ORDER,
                                                   MainPageLocators.ARROW_CANCEL_AN_ORDER,
                                                   MainPageLocators.TEXT_ARROW_CANCEL_AN_ORDER)

    @allure.title('Проверка текста по нажатию стрелочку «Я жизу за МКАДом, привезёте?»')
    def test_chech_text_for_questions_about_great_live_outside_mkad(self, driver):
        driver.get(BasePageUrls.URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.check_text_questions_about_great(self.TEXT_LIVE_OUTSIDE_MKAD,
                                                   MainPageLocators.ARROW_LIVE_OUTSIDE_MKAD,
                                                   MainPageLocators.TEXT_ARROW_LIVE_OUTSIDE_MKAD)

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