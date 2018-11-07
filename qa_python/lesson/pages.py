#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time

from page_objects import PageObject
from page_objects import PageElement
from page_objects import MultiPageElement


class YandexMainPage(PageObject):

    search_text = PageElement(id_='text')
    search_button = PageElement(xpath='//button')

    def __init__(self, web_driver, uri=''):
        super().__init__(web_driver, uri)
        self.get('https://ya.ru')


class YandexSearchResultsPage(YandexMainPage):

    results = MultiPageElement(xpath='//a[contains(@class, "organic__url")]')

    def results_count(self):
        return len(self.results)
