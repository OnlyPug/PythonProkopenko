import pytest
from selenium.webdriver import Chrome

from lesson20.pages.main_page import MainPage
from lesson20.pages.strategy_game_page import StrategyGamePage
from lesson20.pages.header_page import HeaderPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    driver.get("https://gameland.com.ua/")
    yield MainPage(driver)


@pytest.fixture
def strategy(driver):
    driver.get('https://gameland.com.ua/strategii/')
    yield StrategyGamePage(driver)


@pytest.fixture
def header(driver):
    driver.get("https://gameland.com.ua/")
    yield HeaderPage(driver)
