from selenium.webdriver.common.by import By

class MainPageLocators:

    TEXT_QUESTIONS_ABOUT_GREAT = [By.XPATH, "//div[text()='Вопросы о важном']"] # Блок вопросы о важном
    ARROW_HOW_MUCH = [By.ID, 'accordion__heading-0'] #Стрелочка Сколько это стоит? И как оплатить?
    TEXT_ARROW_HOW_MUCH = [By.ID, 'accordion__panel-0'] #Текст в стрелочке Сколько это стоит? И как оплатить?
    ARROW_WANT_SOME_SCOOTER = [By.ID,'accordion__heading-1']#Стрелочка «Хочу сразу несколько самокатов! Так можно?»
    TEXT_ARROW_WANT_SOME_SCOOTER = [By.ID,'accordion__panel-1'] #Текст в стрелочке «Хочу сразу несколько самокатов! Так можно?»
    ARROW_HOW_IS_RENTAL_TIME_CALCULATED = [By.ID, 'accordion__heading-2'] #Стрелочка «Как рассчитывается время аренды?»
    TEXT_ARROW_HOW_IS_RENTAL_TIME_CALCULATED = [By.ID, 'accordion__panel-2'] #Текст в стрелочке «Как рассчитывается время аренды?»
    ARROW_ORDER_SCOOTER_TODAY = [By.ID, 'accordion__heading-3'] #Стрелочка «Можно ли заказать самокат прямо на сегодня?»
    TEXT_ARROW_ORDER_SCOOTER_TODAY = [By.ID, 'accordion__panel-3'] #Текст в стрелочке «Можно ли заказать самокат прямо на сегодня?»
    ARROW_EXTEND_OR_RETURN_SCOOTER = [By.ID, 'accordion__heading-4'] #Стрелочка «Можно ли продлить заказ или вернуть самокат раньше?»
    TEXT_ARROW_EXTEND_OR_RETURN_SCOOTER = [By.ID, 'accordion__panel-4'] #Текст в стрелочке «Можно ли продлить заказ или вернуть самокат раньше?»
    ARROW_CHARGER_WITH_SCOOTER = [By.ID,'accordion__heading-5'] #Стрелочка «Вы привозите зарядку вместе с самокатом?»
    TEXT_ARROW_CHARGER_WITH_SCOOTER = [By.ID,'accordion__panel-5'] #Текст в стрелочке «Вы привозите зарядку вместе с самокатом?»
    ARROW_CANCEL_AN_ORDER = [By.ID, 'accordion__heading-6'] #Стрелочка «Можно ли отменить заказ?»
    TEXT_ARROW_CANCEL_AN_ORDER = [By.ID, 'accordion__panel-6']#Текст в стрелочке «Можно ли отменить заказ?»
    ARROW_LIVE_OUTSIDE_MKAD = [By.ID, 'accordion__heading-7'] #Стрелочка «Я жизу за МКАДом, привезёте?»
    TEXT_ARROW_LIVE_OUTSIDE_MKAD = [By.ID, 'accordion__panel-7'] #Текст в стрелочке «Я жизу за МКАДом, привезёте?»
    LOGO_SCOOTER = [By.XPATH,'//a[contains(@class, "Header_LogoScooter")]']#Логотип Самоката
    LOGO_YANDEX = [By.CLASS_NAME,'Header_LogoYandex__3TSOI']#Логотип Яндекса