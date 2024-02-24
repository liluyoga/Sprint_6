from selenium.webdriver.common.by import By


class AdditionalLocators:
    ACCEPT_COOKIES = [By.XPATH, ".//button[@id='rcc-confirm-button']"]  # кнопка принятия куки Да все привыкли
    DZEN = [By.ID, "dzen-header"]  # хедер страницы Дзен
