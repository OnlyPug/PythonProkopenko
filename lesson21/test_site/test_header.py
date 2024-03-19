import time


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


# Lesson 22

def test_call_us_section(header):
    header.move_on_call_us_section()
    assert header.call_us_section_snow()


def test_call_us_section_call_us_back(header):
    header.move_on_call_us_section()
    assert header.call_us_section_snow()
    header.click_call_us_back()
    assert header.call_us_pop_up_snow()
    header.input_name(text='Anastasiia')
    header.input_number(text='123456789')
    assert header.is_send_button()


def test_open_and_close_login_pop_up(header):
    header.click_login_button()
    assert header.login_pop_up_snow()
    header.click_close_pop_up()
    assert header.pop_up_close()


def test_login_negative_flow(header):
    header.click_login_button()
    assert header.login_pop_up_snow()
    header.input_user_name(text='some.email@ua')
    header.input_user_password(text='123456789')
    assert header.is_login_button()
    header.click_login_user_button()
    assert header.error_shown()


def test_registration_flow(header):
    header.click_login_button()
    assert header.login_pop_up_snow()
    header.click_new_user_button()
    assert header.this_page_registration()
    header.input_first_second_name(text='Anastasiia Prokopenko')
    header.input_new_email_password(text='some.email@ua')
    header.input_new_user_password(text='Strong_password')
    assert header.is_registration_button()


def test_registration_negative_flow(header):
    header.click_login_button()
    assert header.login_pop_up_snow()
    header.click_new_user_button()
    assert header.this_page_registration()
    header.click_registration_user_button()
    assert header.error_registration_shown()


