from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIELD_NAME = [By.XPATH,"//input[@placeholder='* Имя']"] #Поле ввода имени
    FIELD_LAST_NAME = [By.XPATH,"//input[@placeholder='* Фамилия']"] # Поле для ввода фамилия
    FIELD_ADDRESS = [By.XPATH,"//input[@placeholder='* Адрес: куда привезти заказ']"]#Поле для ввода адреса
    FIELD_METRO = [By.XPATH,"//input[@placeholder='* Станция метро']"]#Поле для выбора метро
    DROPDOWN_METRO = [By.XPATH,"(//div[text()='Бульвар Рокоссовского'])[1]"]#Метро из выпадающего списка
    FIELD_PHONE = [By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']"] #Поле для ввода телефона
    BUTTON_NEXT = [By.XPATH,"//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"] #Кнопка далее
    TEXT_ABOUT_RENT = [By.CLASS_NAME,"Order_Header__BZXOb"] #Текст о аренде
    FIELD_WHEN_BRING_SCOOTER = [By.XPATH,"//input[@placeholder='* Когда привезти самокат']"] #Календарь
    DATA_FOR_ORDER = [By.XPATH,"//div[@aria-label='Choose пятница, 28-е марта 2025 г.']"]#Выбор даты
    FIELD_RENTAL_PERIOD = [By.CLASS_NAME,"Dropdown-placeholder"] #Выпающий список с длительностью аренды
    DROPDOWN_RENTAL_PERIOD = [By.XPATH,"//div[text()='четверо суток']"] #Количество дней из выпадающего списка
    CHECKBOX_COLOR_SCOOTER = [By.ID,'black'] #Чекбокс цвет самоката
    FIELD_COMMENT_FOR_COURIER = [By.XPATH,"//input[@placeholder='Комментарий для курьера']"] #Комментарий для курьера
    BUTTON_ORDER = [By.XPATH,"//div[@class='Order_Buttons__1xGrp']/child::button[text()='Заказать']"] #Кнопка Заказать
    BUTTON_YES_FOR_POPUP = [By.XPATH,"//button[text()='Да']"] #Подтверждаем заказ
    BUTTON_WATCH_STATUS = [By.XPATH,'//button[text()="Посмотреть статус"]']#Кнопка посмотреть статус
    BUTTON_ORDER_CANCEL = [By.XPATH,'//div[contains(@class, "Track_OrderInfo")]/button']#Кнопка Отменить заказ