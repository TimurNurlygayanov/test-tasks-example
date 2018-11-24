#!/usr/bin/python3
# -*- encoding=utf8 -*-

# How to run:
#    python3 -m pytest -v --driver Chrome --driver-path /tests/chrome --alluredir ./allure_report
#

import pytest
import allure
from pages import YandexMainPage


@allure.feature('Search on main page')
@pytest.mark.parametrize('word', ['iphone', 'кофеварка'])
def test_yandex_market_search(web_browser, word):
    """ Check that we can find required products on YandexMarket. """

    page = YandexMainPage(web_browser)
    results_page = page.search(word)

    # Verify that default search page shows 48 results:
    assert results_page.results_count() == 48, 'No results found!'
