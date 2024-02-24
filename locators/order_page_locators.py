from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Кнопки
    ORDER_BUTTON_HEADER = [By.XPATH, ".//div[contains(@class, 'Header')]/button[text()='Заказать']"] # кнопка Заказать в хедере
    ORDER_BUTTON_HOME_PAGE = [By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button"] # кнопка Заказать на странице
    BUTTON_NEXT = [By.XPATH,
                   ".//button[contains(@class, 'Button_Button') and text()='Далее']"]  # кнопка Далее при заказе
    ORDER_BUTTON_FINISH = [By.XPATH,
                           ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"]  # кнопка Заказать после заполнения формы заказа
    BUTTON_YES = [By.XPATH,
                  ".//div[contains(@class, 'Order_Buttons')]/button[text()='Да']"]  # кнопка Да при оформлении заказа

    # Текстовые поля
    INPUT_NAME = [By.XPATH, ".//input[contains(@class, 'Input_Input')][@placeholder='* Имя']"] # поле для ввода имени при заказе
    INPUT_LASTNAME = [By.XPATH, ".//input[contains(@class, 'Input_Input')][@placeholder='* Фамилия']"] # поле для ввода фамилии при заказе
    INPUT_ADDRESS = [By.XPATH, ".//input[contains(@class, 'Input_Input')][@placeholder='* Адрес: куда привезти заказ']"] # поле для ввода адреса при заказе
    PHONE_NUMBER = [By.XPATH,
                    ".//input[contains(@class, 'Input_Input')][@placeholder='* Телефон: на него позвонит курьер']"]  # поле для ввода номера телефона при заказе
    COMMENT = [By.XPATH,
               ".//input[contains(@class, 'Input_Input')][@placeholder='Комментарий для курьера']"]  # поля для ввода комментария
    DATE_ORDER = [By.XPATH,
                  ".//input[contains(@class, 'Input_Input')][@placeholder='* Когда привезти самокат']"]  # поле для ввода даты заказа

    # Выпадающие списки и чек-боксы
    SUBWAY_STATION_FIELD = [By.XPATH, ".//div[@class='select-search']"] # поле Станция метро
    SUBWAY_STATION_1 = [By.XPATH, ".//div/ul/li/button[@value='1']/div[text()='Бульвар Рокоссовского']"] # станция метро Бульвар Рокоссовского
    SUBWAY_STATION_2 = [By.XPATH, ".//div/ul/li/button[@value='21']/div[text()='Румянцево']"] # станция метро Румянцево
    RENTAL_PERIOD_FIELD = [By.XPATH, ".//div[@class='Dropdown-control']"]  # поле Срок аренды
    RENTAL_PERIOD_1 = [By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='сутки']"]  # срок аренды сутки
    RENTAL_PERIOD_2 = [By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='двое суток']"]  # срок аренды двое суток
    BLACK_COLOR_CHECKBOX = [By.XPATH, ".//input[@id='black']"]  # цвет самоката чёрный жемчуг
    GREY_COLOR_CHECKBOX = [By.XPATH, ".//input[@id='grey']"]  # цвет самоката серая безысходность

    # Окно после оформления заказа
    ORDER_PLACED = [By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']"] # Заказ оформлен
