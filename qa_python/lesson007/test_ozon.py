#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest

from pages import OzonMainPage


@pytest.mark.parametrize('text', ['печеньки', 'велосипед', 'ipad'])
def test_check_search(text):
    """ Check that search page shows some products for any popular request.

        Steps:
        1) Open main page
        2) Search some products
        3) Verify that we have some results on search page
    """

    main_page = OzonMainPage()
    search_page = main_page.search(text)

    assert search_page.has_results()


def test_check_price_filter():
    """ Check that filters by price works fine.

        Steps:
        1) Open main page and search some word
        2) Apply filters by price
        3) Make sure we have some products on the page
           and that all products have correct price
    """

    main_page = OzonMainPage()
    search_page = main_page.search('книги по тестированию')

    search_page.min_price = 500
    search_page.max_price = 1000
    search_page.apply_filter.click()

    assert search_page.has_results()

    # Verify all prices on search page:
    for price in search_page.products_prices:
        price_int = int(price.replace('&nbsp;', '').replace(' ', ''))
        assert 500 <= price_int <= 1000, 'Wrong price: {0}'.format(price_int)


def test_check_categories():
    """ Check that all categories have some products.

        Steps:
        1) Open main page and search some word
        2) Click each left categories item and verify that this
           category has some products
    """

    main_page = OzonMainPage()
    search_page = main_page.search('велосипед')

    for category in search_page.categories:
        # Select category:
        category.click()

        # Verify we have some products:
        assert search_page.has_results(), 'Category {0} has no products!'.format(category.text)

        # Return to initial search results page:
        search_page.go_back()
