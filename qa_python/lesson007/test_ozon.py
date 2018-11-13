#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest

from selenium.webdriver import ActionChains

from pages import OzonMainPage


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

    assert search_page.has_results()


@pytest.mark.run
def test_check_price_filter(web_browser):
    """ Check that filters by price works fine.

        Steps:
        1) Open main page and search some word
        2) Apply filters by price
        3) Make sure we have some products on the page
           and that all products have correct price
    """

    main_page = OzonMainPage(web_browser)
    search_page = main_page.search('книги по тестированию')

    import time

    search_page.max_price.clear()
    search_page.max_price = 1000

    time.sleep(3)
    search_page.min_price.clear()
    search_page.min_price = 500


    time.sleep(3)

    action = ActionChains(search_page.w)
    action.move_to_element(search_page.apply_filter).click_and_hold().pause(0.5).release().perform()
    # search_page.apply_filter.click()

    assert search_page.has_results()

    time.sleep(30)

    # Verify all prices on search page:
    for price in search_page.products_prices:
        price_number = float(price.text.replace('&nbsp;', '').replace(' ', ''))
        assert 500 <= price_number <= 1000, 'Wrong price: {0}'.format(price_number)


def test_check_categories(web_browser):
    """ Check that all categories have some products.

        Steps:
        1) Open main page and search some word
        2) Click each left categories item and verify that this
           category has some products
    """

    main_page = OzonMainPage(web_browser)
    search_page = main_page.search('велосипед')

    for category in search_page.categories:
        # Select category:
        category.click()

        # Verify that we have some products:
        assert search_page.has_results(), 'Category {0} has no products!'.format(category.text)

        # Return to initial search results page:
        search_page.go_back()
