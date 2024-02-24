from selenium.webdriver.common.by import By


class HeaderPageLocators:
    LOGO_YANDEX = [By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]"] # ссылка-логотип Яндекс
    LOGO_SCOOTER = [By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"] # ссылка-логотип Самокат
