#!/usr/bin/python3
# -*- encoding=utf8 -*-

from pages import AliExpressMainPage
import time


def test_search_check_number_of_results2(web_browser):
    """ Check that on main Ali Express page we have at least 47
        results for popular search requests.
    """

    page = AliExpressMainPage(web_browser)

    search_page = page.search('iphone X')

    assert len(search_page.results) == 47, 'Not enough results found!'
