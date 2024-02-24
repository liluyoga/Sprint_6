from pages.header_page import HeaderPage


class TestHeaderPage:

    def test_redirect_to_dzen_after_click_logo_yandex(self, driver):
        page = HeaderPage(driver)
        actual_result = page.click_on_logo_yandex_and_switch_to_window()
        assert page.check_redirect_to_dzen(actual_result)

    def test_scooter_main_page_after_click_logo_scooter(self, driver):
        page = HeaderPage(driver)
        actual_result = page.click_on_logo_scooter()
        assert page.check_scooter_main_page(actual_result)
