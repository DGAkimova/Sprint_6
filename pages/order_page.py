import allure
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):



    @allure.step('Вводим Имя')
    def set_name(self,name):
        self.find_elements(BasePageLocators.FIELD_NAME).send_keys(name)

    @allure.step('Вводим фамилию')
    def set_last_name(self,last_name):
        self.find_elements(OrderPageLocators.FIELD_LAST_NAME).send_keys(last_name)

    @allure.step('Вводим Адрес')
    def set_address(self,address):
        self.find_elements(OrderPageLocators.FIELD_ADDRESS).send_keys(address)

    @allure.step('Выбираем странцию метро')
    def click_metro_station(self):
        self.find_elements(OrderPageLocators.FIELD_METRO).click()
        self.wait_for_load_element(OrderPageLocators.DROPDOWN_METRO)
        self.find_elements(OrderPageLocators.DROPDOWN_METRO).click()

    @allure.step('Вводим телефон')
    def set_phone(self,phone):
        self.find_elements(OrderPageLocators.FIELD_PHONE).send_keys(phone)

    @allure.step('Нажимаем кнопку далее')
    def click_button_next(self):
        self.find_elements(OrderPageLocators.BUTTON_NEXT).click()

    def set_abonent_data_step1(self,name,last_name,address,phone):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.click_metro_station()
        self.set_phone(phone)
        self.click_button_next()
        self.wait_for_load_element(OrderPageLocators.TEXT_ABOUT_RENT)

    @allure.step('Проверка, что перешли на второй шаг заказа')
    def assert_go_next_step(self):
        assert 'Про аренду' == self.driver.find_element(*OrderPageLocators.TEXT_ABOUT_RENT).text

    @allure.step('Выбираем когда привезти самокат')
    def set_data(self):
        self.find_elements(OrderPageLocators.FIELD_WHEN_BRING_SCOOTER).click()
        self.find_elements(OrderPageLocators.DATA_FOR_ORDER).click()

    @allure.step('Выбираем срок аренды')
    def set_rental_period(self):
        self.find_elements(OrderPageLocators.FIELD_RENTAL_PERIOD).click()
        self.wait_for_load_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD)
        self.find_elements(OrderPageLocators.DROPDOWN_RENTAL_PERIOD).click()

    @allure.step('Выбираем чек-бокс цвет самоката')
    def set_checkbox_color_scooter(self):
        self.find_elements(OrderPageLocators.CHECKBOX_COLOR_SCOOTER).click()

    @allure.step('Вводим комментарий для курьера')
    def set_comment(self,comment):
        self.find_elements(OrderPageLocators.FIELD_COMMENT_FOR_COURIER).send_keys(comment)

    @allure.step('Нажимаем кнопку заказать')
    def click_order_scooter(self):
        self.find_elements(OrderPageLocators.BUTTON_ORDER).click()


    @allure.step('Подтверждаем оформление заказа')
    def click_yes_for_popup_do_you_want_place_order(self):
        self.wait_for_load_element(OrderPageLocators.BUTTON_YES_FOR_POPUP)
        self.find_elements(OrderPageLocators.BUTTON_YES_FOR_POPUP).click()

    @allure.step('Нажимаем на кнопку посмотреть статус')
    def click_watch_status(self):
        self.find_elements(OrderPageLocators.BUTTON_WATCH_STATUS).click()

    @allure.step('Получаем текст с фронта о отмене заказа')
    def get_text_for_front(self,locator):
        return self.find_elements(locator).text

    @allure.step('Сравниваем текст с тем что на фронте')
    def assert_succes_create_order(self, text_for_popup):
        assert text_for_popup == self.get_text_for_front(OrderPageLocators.BUTTON_ORDER_CANCEL)

    def set_abonent_data_step2(self,comment):
        self.set_data()
        self.set_rental_period()
        self.set_checkbox_color_scooter()
        self.set_comment(comment)
        self.click_order_scooter()
        self.click_yes_for_popup_do_you_want_place_order()
        self.wait_for_load_element(OrderPageLocators.BUTTON_WATCH_STATUS)
        self.click_watch_status()
        self.wait_for_load_element(OrderPageLocators.BUTTON_ORDER_CANCEL)