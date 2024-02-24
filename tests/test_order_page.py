from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from data import OrderData
import pytest


class TestOrderPage:

    @pytest.mark.parametrize(
        "order_button, order_data, subway_station, days, rental_period, color",
        [
            [OrderPageLocators.ORDER_BUTTON_HOME_PAGE, OrderData.order_data_1, OrderPageLocators.SUBWAY_STATION_1,
             1, OrderPageLocators.RENTAL_PERIOD_1, OrderPageLocators.GREY_COLOR_CHECKBOX],
            [OrderPageLocators.ORDER_BUTTON_HEADER, OrderData.order_data_2, OrderPageLocators.SUBWAY_STATION_2,
             2, OrderPageLocators.RENTAL_PERIOD_2, OrderPageLocators.BLACK_COLOR_CHECKBOX]
        ]
    )
    def test_order_by_order_button(self, driver, order_button, order_data, subway_station, days, rental_period, color):
        page = OrderPage(driver)

        actual_result = page.order_scooter(order_button, order_data.get('first_name'), order_data.get('last_name'),
                                           order_data.get('address'), subway_station, order_data.get('phone'), days,
                                           rental_period, color, order_data.get('comment'))

        assert page.check_the_order_placed(actual_result)
