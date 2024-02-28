from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()