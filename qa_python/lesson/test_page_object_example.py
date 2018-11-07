#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time
from pages import YandexMainPage
from pages import YandexSearchResultsPage


def test_search_some_long_text(selenium):
    page = YandexMainPage(selenium)

    page.search_text = 'a' * 1000
    page.search_button.click()

    time.sleep(5)

    search_page = YandexSearchResultsPage(page.w)
    assert search_page.results_count() == 12
