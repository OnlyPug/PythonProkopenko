
def test_main_page(main_page):
    assert main_page.this_main_page


# lesson 21
# re-writte function
def test_click_on_strategy(main_page):
    strategy_page = main_page.click_strategy()
    assert strategy_page.this_page_strategy_game()


# lesson 22

def test_navigation_new(main_page):
    assert main_page.this_main_page()
    main_page.check_navigation()
    assert main_page.this_navigation_meny_board_game()


def test_creator(main_page):
    main_page.clik_on_logo_new_era()
    assert main_page.this_page_new_era()
    main_page.click_back()
    assert main_page.this_main_page()
    main_page.clik_on_igames()
    assert main_page.this_page_igames()
    main_page.click_back()
    assert main_page.this_main_page()
    main_page.clik_on_logo_fealindigo()
    assert main_page.this_page_fealindigo()
    main_page.click_back()
    assert main_page.this_main_page()
    main_page.clik_on_logo_game_seven()
    assert main_page.this_page_game_seven()
    main_page.click_back()
    assert main_page.this_main_page()


def test_creator_game_show_more(main_page):
    main_page.click_show_more_button()
    assert main_page.more_is_show


def test_sale(main_page):
    pay_page = main_page.click_sale_method()
    assert pay_page.this_page_sale()


def test_carousel(main_page):
    main_page.click_on_carousel_page()
    main_page.click_next()
    main_page.click_prev()
    assert main_page.carouse()
