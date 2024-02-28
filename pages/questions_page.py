import allure
from pages.base_page import BasePage
from locators.questions_page_locators import QuestionsLocators
from locators.additional_locators import AdditionalLocators


class QuestionsPage(BasePage):

    @allure.step("Открываем страницу. Переходим к Важным вопросам, кликаем на вопрос.")
    def click_to_question_get_answer(self, num):
        self.accept_cookies(AdditionalLocators.ACCEPT_COOKIES)
        self.scroll_down()
        question_locator = self.format_locator(QuestionsLocators.QUESTION, num)
        answer_locator = self.format_locator(QuestionsLocators.ANSWER, num)
        self.click_on_element(question_locator)
        return self.get_text_from_element(answer_locator)

    @staticmethod
    @allure.step("Проверяем ответ на вопрос.")
    def check_answer_value(actual_result, expected_result):
        return actual_result == expected_result
