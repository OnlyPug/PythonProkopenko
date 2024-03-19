import pytest
from selenium.webdriver import Chrome

from lesson21.pages.main_page import MainPage
from lesson21.pages.strategy_game_page import StrategyGamePage
from lesson21.pages.product_page import ProductPage
from lesson21.pages.header_page import HeaderPage
from lesson21.pages.comics_book_page import ComicsBookPage


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


@pytest.fixture
def product(driver):
    driver.get("https://gameland.com.ua/nanty-narking.-veliki-spodivannya-ukr./")
    yield ProductPage(driver)


@pytest.fixture
def comics_book_page(driver):
    driver.get("https://gameland.com.ua/komiksi-ta-knigi/")
    yield ComicsBookPage(driver)


