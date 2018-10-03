#!/usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_wait import wait_for_page_loaded

BROWSERS = []


def start_browsers():
    global BROWSERS

    chrome_options = Options()
    # chrome_options.add_argument("--window-size=1920x1080")
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--log-level=DEBUG')

    for i in range(1):
        browser = webdriver.Chrome(executable_path='/tests/chrome',
                                   chrome_options=chrome_options,
                                   service_args=["--log-path=/tmp/chrome.log"])

        BROWSERS.append(browser)


def get_browser():
    global BROWSERS

    while BROWSERS == []:
        time.sleep(0.3)

    return BROWSERS.pop()


# Start pool of browsers:
start_browsers()

# Get one browser
br = get_browser()

# Open Yandex Market page:
br.get('https://market.yandex.ru/catalog/54544/list?hid=91013&track=menuleaf')

elements = br.find_elements_by_xpath('//div[@class="n-snippet-card2__title"]')
br.get_screenshot_as_file('tmp.png')

# Set "show 12 elements on page"
drop_down = br.find_element_by_xpath('//*[@role="listbox"]')
drop_down.click()
xpath = '//span[@class="select__text" and text()="Показывать по 12"]'
br.find_element_by_xpath(xpath).click()

wait_for_page_loaded(br)

elements2 = br.find_elements_by_xpath('//div[@class="n-snippet-card2__title"]')

br.get_screenshot_as_file('tmp2.png')

a = len([e for e in elements])
b = len([e for e in elements2])

assert a == b

print(a, b)

# Return browser to the pool:
BROWSERS.append(br)
