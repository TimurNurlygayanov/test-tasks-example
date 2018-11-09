#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time

from page_objects import PageObject
from page_objects import PageElement
from page_objects import MultiPageElement


class OzonMainPage(PageObject):

    search_text = PageElement(class_name='search-input')
    search_btn = PageElement(xpath='//button[@data-test-id="header-search-go"]')

    def __init__(self, web_driver, uri=''):
        super().__init__(web_driver, uri)
        self.get('https://www.ozon.ru/')

    def search(self, text):
        self.search_text = text
        self.search_btn.click()
        return OzonSearchPage(self.w)


class OzonSearchPage(PageObject):

    min_price = PageElement(xpath='//input[@data-test-id="range-filter-from-input"]')
    max_price = PageElement(xpath='//input[@data-test-id="range-filter-to-input"]')
    apply_filter = PageElement(xpath='//input[@data-test-id="range-filter-show"]')
    products_prices = MultiPageElement(xpath='//span[@class="price-number"]/span')
    results_links = MultiPageElement(class_name='text-link name-link')
    categories = MultiPageElement(xpath='//input[@data-test-id="results-navi-level2"]')
    filter_new_products = PageElement(xpath='//span[contains(text(), "Новинки")]')
    filter_popular_products = PageElement(xpath='//span[contains(text(), "Бестселлеры")]')
    filter_low_price_products = PageElement(xpath='//span[contains(text(), "Уцененный товар")]')
    filter_high_rate_products = PageElement(xpath='//span[contains(text(), "Высокий рейтинг")]')

    def has_results(self):
        return len(self.results_links) > 0

    def go_back(self):
        self.w.back()
