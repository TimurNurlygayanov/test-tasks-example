#!/usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
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

br.get("https://todomvc4tasj.herokuapp.com/")
element = br.find_element_by_xpath("//*[@id='new-todo']")
element.send_keys("test")
time.sleep(1)
element.send_keys(Keys.ENTER)


br.get_screenshot_as_file('tmp2.png')
element2 = br.find_element_by_css_selector("ul.todo-list > li")
