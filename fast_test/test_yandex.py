#!/usr/bin/python3
# -*- encoding=utf8 -*-

# How to run:
#    python3 -m pytest -v --driver Chrome --driver-path ~/chrome
#

import time
import pytest


def test_yandex_electronika_click(web_browser):

    web_browser.get('https://market.yandex.ru/')
    link = web_browser.find_element_by_xpath("//span[contains(text(),'Электроника')]")
    link.click()

    time.sleep(10)
