

def test_main_page(main_page):
    assert main_page.this_main_page


def test_click_on_strategy(main_page):
    main_page.click_strategy()
    assert main_page.driver.title == 'Стратегічні настільні ігри купити Україна ➤ Інтернет-магазин Gameland | Київ, Одеса'
