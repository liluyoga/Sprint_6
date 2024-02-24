from selenium.webdriver.common.by import By


class QuestionsLocators:
    QUESTION = [By.XPATH, ".//div[@id='accordion__heading-{}']"] # важный вопрос
    ANSWER = [By.XPATH, ".//div[@id='accordion__panel-{}']/p"] # ответ
