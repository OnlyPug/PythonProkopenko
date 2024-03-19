import pytest
from lesson21.core import ComicsBookLocators
from lesson21.core.data_comics import board_game, genre_game


@pytest.mark.parametrize("navigation,list_of_navigation",
                         [(ComicsBookLocators.locator_navigation_genre_game, genre_game),
                          (ComicsBookLocators.locator_navigation_board_game, board_game)])
def test_navigation_test(comics_book_page, navigation, list_of_navigation):
    comics_book_page.check_navigation_test(navigation, list_of_navigation)
