from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
from locators.additional_locators import AdditionalLocators


class HeaderPage(BasePage):

    def click_on_logo_yandex_and_switch_to_window(self):
        self.click_on_element(HeaderPageLocators.LOGO_YANDEX)
        self.switch_to_window(1)
        return self.get_current_url(AdditionalLocators.DZEN)

    @staticmethod
    def check_redirect_to_dzen(actual_result):
        return 'dzen.ru' in actual_result

    def click_on_logo_scooter(self):
        self.click_on_element(HeaderPageLocators.LOGO_SCOOTER)
        return self.get_current_url(HeaderPageLocators.LOGO_SCOOTER)

    @staticmethod
    def check_scooter_main_page(actual_result):
        return actual_result == 'https://qa-scooter.praktikum-services.ru/'