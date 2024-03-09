import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_open_site_booking_uz():
    driver = Chrome()
    driver.maximize_window()
    url = 'https://www.google.com/'
    driver.get(url)
    # Accept google notification
    accept_google_locator = '//button[@id="W0wltc"]'
    if driver.find_element(By.XPATH, accept_google_locator):
        driver.find_element(By.XPATH, accept_google_locator).click()
    assert driver.current_url == url
    search_locator = '//textarea[@class="gLFyf"]'
    search_element = driver.find_element(by='xpath', value=search_locator)
    search_element.send_keys('booking uz')
    search_element.send_keys(Keys.ENTER)
    change_language_locator = '//a[text()="Change to English"]'
    # Change on english language google
    if driver.find_element(by='xpath', value=change_language_locator):
        driver.find_element(by='xpath', value=change_language_locator).click()
    booking_site_locator = '//div[@class="GyAeWb"]//div[@id="rso"]//div[@jscontroller="SC7lYd"][1]'
    driver.find_element(By.XPATH, booking_site_locator).click()
    # Skip Google Translate page
    google_transleter_locator = '//div[@class="ueocBf"]/a'
    if driver.find_element(by='xpath', value=google_transleter_locator):
        driver.find_element(by='xpath', value=google_transleter_locator).click()
    assert driver.current_url.startswith('https://booking.uz.gov.ua/uk/')
    driver.quit()


def test_quote():
    driver = Chrome()
    driver.maximize_window()
    url = 'https://www.minimizemymess.com/random-quote-generator'
    driver.get(url)
    assert driver.current_url.startswith('https://www.minimizemymess.com')
    # Accept pop-up
    accept_button_locator = '//div[text()="Accept"]'
    if driver.find_element(by='xpath', value=accept_button_locator):
        driver.find_element(by='xpath', value=accept_button_locator).click()

    text_box_locator = '//div[@id="box2"]'
    locate = driver.find_element(by='xpath', value=text_box_locator)
    driver.execute_script("arguments[0].scrollIntoView(true);", locate)
    driver.implicitly_wait(5)
    # reload page
    driver.refresh()
    # see you new quote
    driver.implicitly_wait(5)
    driver.quit()


def test_login_negative():
    driver = Chrome()
    driver.maximize_window()
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver.get(url)
    assert driver.current_url.startswith('https://opensource-demo')
    driver.implicitly_wait(5)
    # Select title text and Cntr+c text
    login_text_locator = '//h5[@class="oxd-text oxd-text--h5 orangehrm-login-title"]'
    locate = driver.find_element(by='xpath', value=login_text_locator)
    action = ActionChains(driver)
    action.double_click(locate).perform()
    action.key_down(Keys.CONTROL).key_down('c').key_up(Keys.CONTROL).perform()
    # Input username with Cntr+v
    username_text_locator = '//input[@name="username"]'
    driver.find_element(by='xpath', value=username_text_locator).click()
    action.key_down(Keys.CONTROL).key_down('v').key_up(Keys.CONTROL).perform()
    # Input password with Cntr+v
    username_text_locator = '//input[@type="password"]'
    driver.find_element(by='xpath', value=username_text_locator).click()
    action.key_down(Keys.CONTROL).key_down('v').key_up(Keys.CONTROL).perform()
    # Click submit
    button_locator = '//button[@type="submit"]'
    driver.find_element(by='xpath', value=button_locator).click()
    # Get text and assert
    driver.implicitly_wait(2)
    text_locator = '//p[text()="Invalid credentials"]'
    assert driver.find_element(by='xpath', value=text_locator)
    driver.quit()


def test_pagination():
    driver = Chrome()
    driver.maximize_window()
    url = 'https://prodrone.com.ua/drony/1180/'
    driver.get(url)
    assert driver.current_url.startswith('https://prodrone.com.ua')
    # Select page №3
    page_locator = '//div[@class="pager__container"]//a[2]'
    driver.find_element(by='xpath', value=page_locator).click()
    cheak_url = 'https://prodrone.com.ua/drony/1180/filter/page=3/'
    time.sleep(5)
    assert cheak_url == driver.current_url
    driver.quit()


def test_max_price():
    driver = Chrome()
    driver.maximize_window()
    url = 'https://prodrone.com.ua/drony/1180/'
    driver.get(url)
    assert driver.current_url.startswith('https://prodrone.com.ua')
    driver.implicitly_wait(5)
    input_locator = '//div[@class="filter-price"]//input[2]'
    locate = driver.find_element(by='xpath', value=input_locator)
    # Select title text and Cntr+c text
    action = ActionChains(driver)
    action.double_click(locate).perform()
    action.key_down(Keys.CONTROL).key_down('c').key_up(Keys.CONTROL).perform()
    # Input username with Cntr+v
    username_text_locator = '//div[@class="filter-price"]//input[1]'
    driver.find_element(by='xpath', value=username_text_locator).click()
    action.key_down(Keys.CONTROL).key_down('v').key_up(Keys.CONTROL).perform()
    # Click 'OK' button
    ok_button = '//button[@type="submit"]/span[@class="btn-content"]'
    driver.find_element(by='xpath', value=ok_button).click()
    # assert max price
    price_text_locator = '//div[@class="catalogCard-price"]'
    price_text = driver.find_element(by='xpath', value=price_text_locator)
    text = price_text.text
    assert text == '329 999 грн'
    driver.quit()

