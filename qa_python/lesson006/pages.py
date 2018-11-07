#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time

from page_objects import PageObject
from page_objects import PageElement
from page_objects import MultiPageElement


class AliExpressMainPage(PageObject):

    search_text = PageElement(id_='search-key')
    search_btn = PageElement(class_name='search-button')
    banner_close = PageElement(class_name='close-layer')

    def __init__(self, web_driver, uri=''):
        super().__init__(web_driver, uri)
        self.get('https://ru.aliexpress.com')
        self.banner_close.click()
        time.sleep(2)

    def search(self, text):
        self.search_text = text
        self.search_btn.click()
        return AliExpressSearchPage(self.w)


class AliExpressSearchPage(PageObject):

    search_field = PageElement(id_='search-key')
    search_btn = PageElement(class_name='search-button')
    results = MultiPageElement(xpath='//*[contains(@class, "history-item product")]')


class TMallMainPage(AliExpressMainPage):

    def __init__(self, web_driver, uri=''):
        super().__init__(web_driver, uri)
        self.get('https://tmall.aliexpress.com')
        self.banner_close.click()
        time.sleep(2)
