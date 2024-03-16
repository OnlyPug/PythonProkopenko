# lesson 21

def test_click_on_first_element(strategy):
    product_page = strategy.click_on_first_element()
    assert product_page.this_page()


def test_click_comments(product):
    product.click_on_comment()
    assert product.comments_opened


# Function without 'send'
def test_click_input_text_for_comments(product):
    product.click_on_comment()
    product.input_name()
    product.input_email()
    product.input_text_comment()
    product.click_on_stars()
    assert product.check_one_stars


def test_pdf(product):
    product.click_on_pdf_button()
    assert product.this_pdf_page
    product.close_second_tab()


def test_login_page(product):
    product.click_next_btn()
    assert product.check_page2()
    product.click_next_btn()
    assert product.check_page3
    product.click_next_btn()
    assert product.check_page4
    product.click_next_btn()
    assert product.check_page5
    product.click_next_btn()
    assert product.check_page6


def test_click_buy(product):
    basket_page = product.on_product_page()
    assert basket_page.this_page()
