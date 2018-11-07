#!/usr/bin/python3
# -*- encoding=utf8 -*-

from pages import AliExpressPage
import time


def test_search_simple_example(web_browser):
    page = AliExpressPage(web_browser)

    page.search_field = 'iphone X'

    page.search_btn.click()

    page.w.save_screenshot('test.png')

    assert len(page.results) == 47, 'Not enough results found!'
