from lesson21.pages.product_page import ProductPage


def test_click_buy_and_check_product(product):
    basket_page = product.on_product_page()
    assert basket_page.this_page_basket()
    basket_page.product_chouse()


def test_add_more(product):
    basket_page = product.on_product_page()
    assert basket_page.this_page_basket()
    basket_page.click_add_this_product()
    assert int(basket_page.check_value_basket()) == 2


def test_click_cross_button(product):
    basket_page = product.on_product_page()
    assert basket_page.this_page()
    basket_page.click_cross()
    product_page = ProductPage(product.driver)
    assert product_page.this_page()


def test_click_back_button(product):
    basket_page = product.on_product_page()
    assert basket_page.this_page()
    basket_page.click_back()
    product_page = ProductPage(product.driver)
    assert product_page.this_page()
