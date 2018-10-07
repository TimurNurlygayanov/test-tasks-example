#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is a simple example of PyTest test case with Selenium
# Note: you should install pytest-selenium package.
# 
# To run test cases, execute the following commands:
# cd qa_python
# pytest -v --driver Chrome --driver-path /usr/bin/chromedriver test_pytest_002.py
#

import pytest


def test_ya_page_title(web_browser):
    """ This is simple test case shows how PyTest integrated
        with Selenium.

        Note: you should install pytest-selenium package.

        Note: parameter 'web_browser' - is the fixture,
              which described in file conftest_001.py (need to rename
              conftest_001.py to conftest.py to make it work).

              This fixture will automatically start browser and return
              WebDriver element to the test case.
    """

    web_browser.get('https://ya.ru')

    assert "Яндекс" in web_browser.title
