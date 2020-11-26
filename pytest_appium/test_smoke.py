import os
from appium import webdriver


def set_up():
    d_caps = {}
    d_caps['platformName'] = 'iOS'
    d_caps['platformVersion'] = '14.0'
    d_caps['deviceName'] = 'iPhone 7'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', d_caps)


set_up()
