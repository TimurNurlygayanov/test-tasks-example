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


class OzonMainPage(PageObject):

    search_text_field = PageElement(xpath='(//input)[1]')
    search_btn = PageElement(xpath='//div[@class="bFlatButton mSearchButton"]')

    def __init__(self, web_driver, uri=''):
        super().__init__(web_driver, uri)
        self.get('https://www.ozon.ru/')

    def search(self, text):
        self.search_text_field = text

        action = ActionChains(self.w)
        action.click_and_hold(self.search_btn).\
            pause(0.5).release(self.search_btn).perform()

        wait_page_loaded(self.w)

        return OzonSearchPage(self.w)


class OzonSearchPage(PageObject):

    min_price = PageElement(xpath='//input[@data-test-id="range-filter-from-input"]')
    max_price = PageElement(xpath='//input[@data-test-id="range-filter-to-input"]')
    apply_filter = PageElement(xpath='//button[contains(text(), "Показать")]')
    products_prices = MultiPageElement(xpath='//span[@class="price-number"]/span')
    results_links = MultiPageElement(xpath='//a[@class="text-link name-link"]')
    categories = MultiPageElement(xpath='//a[@class="category-link"]')
    filter_new_products = PageElement(xpath='//span[contains(text(), "Новинки")]')
    filter_popular_products = PageElement(xpath='//span[contains(text(), "Бестселлеры")]')
    filter_low_price_products = PageElement(xpath='//span[contains(text(), "Уцененный товар")]')
    filter_high_rate_products = PageElement(xpath='//span[contains(text(), "Высокий рейтинг")]')

    def __init__(self, web_driver, uri=''):
        super().__init__(web_driver, uri)
        web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def has_results(self):
        return len(self.results_links) > 0

    def go_back(self):
        self.w.back()
        wait_page_loaded(self.w)

    def wait_page_loaded(self):
        wait_page_loaded(self.w)
