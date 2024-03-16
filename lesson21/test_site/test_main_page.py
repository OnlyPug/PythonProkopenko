def test_main_page(main_page):
    assert main_page.this_main_page


# lesson 21
# re-writte function
def test_click_on_strategy(main_page):
    strategy_page = main_page.click_strategy()
    assert strategy_page.this_page_strategy_game()
