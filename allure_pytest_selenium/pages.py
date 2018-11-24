#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time

from selenium.webdriver import ActionChains
from page_objects import PageObject
from page_objects import PageElement
from page_objects import MultiPageElement


def wait_page_loaded(driver):
    time.sleep(2)
    page_loaded = False

    while not page_loaded:
        page_loaded = driver.execute_script("return document.readyState == 'complete';")
        time.sleep(0.1)


class YandexMainPage(PageObject):

    search_text = PageElement(name='text')
    search_button = PageElement(xpath='//span/button')

    def __init__(self, web_driver, uri=''):
        super().__init__(web_driver, uri)
        self.get('https://market.yandex.ru')
        wait_page_loaded(self.w)

    def search(self, text):
        self.search_text = text
        self.search_button.click()

        wait_page_loaded(self.w)

        return ProductsListPage(self.w)


class ProductsListPage(PageObject):

    results = MultiPageElement(xpath='//div[@class="n-snippet-cell2__title"]/a')

    def results_count(self):
        return len(self.results)
