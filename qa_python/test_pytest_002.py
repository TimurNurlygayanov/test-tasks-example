#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is a simple example of PyTest test case with Selenium
#
# To run test cases, execute the following commands:
# cd qa_python
# pytest -v --driver Chrome --driver-path /usr/bin/chromedriver test_pytest_002.py
#

import pytest


def test_ya_page_title(web_browser):
    """ This is simple test case to show how PyTest integrated
        with Selenium.

        Note: parameter 'web_element' - is the fixture of PyTest,
              which will automaticall start browser and return
              WebDriver element to the test case.
    """

    web_browser.get('https://ya.ru')

    assert "Яндекс" in browser.title
