from selenium.webdriver.common.by import By

class BasePageLocators:
    BUTTON_ORDER = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/child::button[@class='Button_Button__ra12g']"] #Кнопка Заказать вверху главной
    FIELD_NAME = [By.XPATH,"//input[@placeholder='* Имя']"] #Поле ввода имени

