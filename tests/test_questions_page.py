import allure

from pages.questions_page import QuestionsPage
from data import AnswerValue
import pytest


class TestQuestionsPage:

    @allure.title("Проверка соответствия ответов на Важные вопросы")
    @pytest.mark.parametrize(
        "num, answer_value",
        [
            [0, AnswerValue.ANSWER_1],
            [1, AnswerValue.ANSWER_2],
            [2, AnswerValue.ANSWER_3],
            [3, AnswerValue.ANSWER_4],
            [4, AnswerValue.ANSWER_5],
            [5, AnswerValue.ANSWER_6],
            [6, AnswerValue.ANSWER_7],
            [7, AnswerValue.ANSWER_8]
        ]
    )
    def test_important_questions(self, driver, num, answer_value):
        page = QuestionsPage(driver)

        actual_result = page.click_to_question_get_answer(num)

        assert page.check_answer_value(actual_result, answer_value)
