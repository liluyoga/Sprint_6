from locators.order_page_locators import OrderPageLocators
class AnswerValue:
    ANSWER_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    ANSWER_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    ANSWER_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    ANSWER_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


class OrderData:
    order_data_1 = {'first_name': 'Павел', 'last_name': 'Сибирский', 'address': 'Ленина 17', 'phone': '+79991123453', 'comment': 'позвонить за 1 час'}
    order_data_2 = {'first_name': 'Виктория', 'last_name': 'Медведева', 'address': 'Тверская 76, квартира 16', 'phone': '89005577984', 'comment': ''}
    subway_stations = [OrderPageLocators.SUBWAY_STATION_1, OrderPageLocators.SUBWAY_STATION_2]
    rental_period = [OrderPageLocators.RENTAL_PERIOD_1, OrderPageLocators.RENTAL_PERIOD_2]
    color = [OrderPageLocators.GREY_COLOR_CHECKBOX, OrderPageLocators.BLACK_COLOR_CHECKBOX]
    order_button = [OrderPageLocators.ORDER_BUTTON_HOME_PAGE, OrderPageLocators.ORDER_BUTTON_HEADER]