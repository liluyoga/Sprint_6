import allure
from pages.order_page import OrderPage
from data import OrderData
import pytest


class TestOrderPage:

    @allure.title("Проверка оформления заказа самоката через кнопку Заказать")
    @pytest.mark.parametrize(
        "order_button, order_data, subway_station, days, rental_period, color",
        [
            [OrderData.order_button[0], OrderData.order_data_1, OrderData.subway_stations[0],
             1, OrderData.rental_period[0], OrderData.color[0]],
            [OrderData.order_button[1], OrderData.order_data_2, OrderData.subway_stations[1],
             2, OrderData.rental_period[1], OrderData.color[1]]
        ]
    )
    def test_order_by_order_button(self, driver, order_button, order_data, subway_station, days, rental_period, color):
        page = OrderPage(driver)

        actual_result = page.order_scooter(order_button, order_data.get('first_name'), order_data.get('last_name'),
                                           order_data.get('address'), subway_station, order_data.get('phone'), days,
                                           rental_period, color, order_data.get('comment'))

        assert page.check_the_order_placed(actual_result)
