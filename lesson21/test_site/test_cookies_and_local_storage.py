
def test_main_page_get_cookies(main_page):
    assert main_page.this_main_page
    main_page.cookies_main_page()


def test_add_cookie_and_check(main_page):
    assert main_page.this_main_page
    main_page.cookies_main_page()
    main_page.add_cookies_main_page({'name': 'Game_page', 'value': 'this is board game'})


def test_add_local_storage(main_page):
    assert main_page.this_main_page
    main_page.cookies_main_page()
    main_page.add_or_change_local_storage_main_page(name='Game', value='CS')


def test_change_local_storage(main_page):
    assert main_page.this_main_page
    main_page.cookies_main_page()
    main_page.add_or_change_local_storage_main_page(name='inlineSVGrev', value='i don`t know what is it')




