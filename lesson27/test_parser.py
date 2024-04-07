def test_this_boar_game_parser(parser):
    assert parser.this_page_board_game(url='https://geekach.com.ua/zhanry/na-udachu/')


def test_count_product(parser):
    count_product = parser.all_product_on_page(url='https://geekach.com.ua/zhanry/na-udachu/')
    assert int(count_product) == 20


def test_save_all_links_on_first_page(parser):
    parser.save_all_products_to_file(url='https://geekach.com.ua/zhanry/na-udachu/')


def test_pagination_and_save_to_json(parser):
    parser.collect_product_links()


def test_product_with_information(parser):
    parser.information_about_product()
