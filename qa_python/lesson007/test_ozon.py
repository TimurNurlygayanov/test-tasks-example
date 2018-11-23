#!/usr/bin/python3
# -*- encoding=utf8 -*-

# How to run:
#    python3 -m pytest -v --driver Chrome --driver-path /tests/chrome
#

import time
import pytest

from selenium.webdriver import ActionChains

from pages import OzonMainPage


def convert_price(price):
    print(price)

    price_number = 0

    try:
        price_number = float(price.replace('&nbsp;', '').replace(' ', ''))
    except:
        pass

    return price_number


@pytest.mark.ozon_smoke_ui
@pytest.mark.parametrize('text', ['печеньки', 'велосипед', 'ipad'])
def test_check_search(web_browser, text):
    """ Check that search page shows some products for any popular request.

        Steps:
        1) Open main page
        2) Search some products
        3) Verify that we have some results on search page
    """

    main_page = OzonMainPage(web_browser)
    search_page = main_page.search(text)

    time.sleep(5)  # for demo purposes only
                   # do not repeat with real tests :)

    assert search_page.has_results()


@pytest.mark.ozon_smoke_ui
def test_check_price_filter_min(web_browser):
    """ Check that filter by minimum price works fine.

        Steps:
        1) Open main page and search some word
        2) Apply filters by price
        3) Make sure we have some products on the page
           and that all products have correct price
    """

    main_page = OzonMainPage(web_browser)
    search_page = main_page.search('книги по тестированию')

    time.sleep(5)  # for demo purposes only
                   # do not repeat with real tests :)

    search_page.min_price.clear()
    search_page.min_price = 500

    time.sleep(5)  # for demo purposes only
                   # do not repeat with real tests :)

    action = ActionChains(search_page.w)
    action.move_to_element(search_page.apply_filter).click_and_hold().\
        pause(0.5).release().perform()

    # Make sure we have some results on the page:
    assert search_page.has_results()

    time.sleep(5)  # for demo purposes only
                   # do not repeat with real tests :)

    # Verify all prices on search page:
    for price in search_page.products_prices:
        if price.text:
            assert 500 <= convert_price(price.text), 'Wrong price: {0}'.format(price.text)


@pytest.mark.ozon_smoke_ui
def test_check_price_filter_max(web_browser):
    """ Check that filters by maximum price works fine.

        Steps:
        1) Open main page and search some word
        2) Apply filters by price
        3) Make sure we have some products on the page
           and that all products have correct price
    """

    main_page = OzonMainPage(web_browser)
    search_page = main_page.search('книги по тестированию')

    time.sleep(5)  # for demo purposes only
                   # do not repeat with real tests :)

    search_page.max_price.clear()
    search_page.max_price = 1000

    time.sleep(5)  # for demo purposes only
                   # do not repeat with real tests :)

    action = ActionChains(search_page.w)
    action.move_to_element(search_page.apply_filter).click_and_hold().\
        pause(0.5).release().perform()

    # Make sure we have some results on the page:
    assert search_page.has_results()

    time.sleep(5)  # for demo purposes only
                   # do not repeat with real tests :)

    # Verify all prices on search page:
    for price in search_page.products_prices:
        if price.text > '':
            assert convert_price(price.text) <= 1000, 'Wrong price: {0}'.format(price.text)


@pytest.mark.run
@pytest.mark.ozon_smoke_ui
# @pytest.mark.skip(reason='Need to debug')
def test_check_categories(web_browser):
    """ Check that all categories have some products.

        Steps:
        1) Open main page and search some word
        2) Click each left categories item and verify that this
           category has some products
    """

    main_page = OzonMainPage(web_browser)
    search_page = main_page.search('велосипед')

    categories = search_page.categories
    for i, _ in enumerate(categories):
        category = categories[i]

        # Select category:
        category.click()

        search_page.wait_page_loaded()

        # Verify that we have some products:
        assert search_page.has_results(), 'Category {0} has no products!'.format(category.text)

        # Return to initial search results page:
        search_page.go_back()
        categories = search_page.categories
