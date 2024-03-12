
def test_header_search(header):
    header.input_text_on_search()
    header.wait_search_selection()
    header.click_on_search_button()
    header.page_load()
    assert header.this_page_after_search_mafia()


def test_header_about_us(header):
    header.click_on_about_us_button()
    assert header.this_page_about_us()


def test_header_blogs(header):
    header.click_blogs_news_button()
    assert header.this_page_blogs_news()


def test_header_vidavnitstvo(header):
    header.click_vidavnitstvo_button()
    assert header.this_page_vidavnitstvo()
