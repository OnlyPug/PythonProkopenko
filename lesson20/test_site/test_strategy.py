def test_strategy_for_main(strategy):
    assert strategy.this_page_strategy_game()


def test_strategy_sort_by_min_price(strategy):
    strategy.click_lover_prise()
    strategy.load_page(page=strategy.wait_page)
    assert strategy.driver.current_url == 'https://gameland.com.ua/strategii/filter/sort_price=ASC/'


def test_strategy_sort_by_max_price(strategy):
    strategy.click_max_prise()
    strategy.load_page(page=strategy.wait_page)
    assert strategy.driver.current_url == 'https://gameland.com.ua/strategii/filter/sort_price1=DESC/'


def test_strategy_sort_by_popular(strategy):
    strategy.click_popular()
    strategy.load_page(page=strategy.wait_page)
    assert strategy.driver.current_url == 'https://gameland.com.ua/strategii/'


def test_strategy_sort_by_name(strategy):
    strategy.click_name()
    strategy.load_page(page=strategy.wait_page)
    assert strategy.driver.current_url == 'https://gameland.com.ua/strategii/filter/sort_title=ASC/'


def test_click_on_cheak_box(strategy):
    strategy.click_on_check_box()
    strategy.load_page(page=strategy.page_check_box)
    assert strategy.driver.current_url == 'https://gameland.com.ua/strategii/filter/mexanika=1/'
