from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.additional_locators import AdditionalLocators
import datetime
import keyboard


class OrderPage(BasePage):

    def fill_text_field_in_the_order_form(self, field_locator, text_value):
        self.input_value_to_field(field_locator, text_value)

    def select_subway_station(self, field_locator, station_locator):
        self.click_on_element(field_locator)
        self.scroll_and_click_on_element(station_locator)

    def fill_date_order_in_the_order_form(self, field_locator, days):
        date = datetime.datetime.today() + datetime.timedelta(days=days)
        date = date.strftime("%d.%m.%Y")
        self.input_value_to_field(field_locator, date)
        keyboard.press('Esc')

    def select_rental_period(self, field_locator, period_locator):
        self.click_on_element(field_locator)
        self.click_on_element(period_locator)

    def select_color(self, color_locator):
        self.click_on_element(color_locator)

    @staticmethod
    def check_the_order_placed(actual_result):
        return 'Заказ оформлен' in actual_result

    def order_scooter(self, order_button, first_name, last_name, address, subway_station, phone, days, rental_period, color, comment):
        self.accept_cookies(AdditionalLocators.ACCEPT_COOKIES)
        self.click_on_element(order_button)
        self.fill_text_field_in_the_order_form(OrderPageLocators.INPUT_NAME, first_name)
        self.fill_text_field_in_the_order_form(OrderPageLocators.INPUT_LASTNAME, last_name)
        self.fill_text_field_in_the_order_form(OrderPageLocators.INPUT_ADDRESS, address)
        self.select_subway_station(OrderPageLocators.SUBWAY_STATION_FIELD, subway_station)
        self.fill_text_field_in_the_order_form(OrderPageLocators.PHONE_NUMBER, phone)
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)
        self.fill_date_order_in_the_order_form(OrderPageLocators.DATE_ORDER, days)
        self.select_rental_period(OrderPageLocators.RENTAL_PERIOD_FIELD, rental_period)
        self.select_color(color)
        self.fill_text_field_in_the_order_form(OrderPageLocators.COMMENT, comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_FINISH)
        self.click_on_element(OrderPageLocators.BUTTON_YES)
        return self.get_text_from_element(OrderPageLocators.ORDER_PLACED)
