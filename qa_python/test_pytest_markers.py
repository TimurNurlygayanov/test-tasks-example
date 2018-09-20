#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is the very simple example of PyTest tests with
# markers. Markers allow you to select some test cases
# by some tag. Each test case can have several tags.
#
# How To Run all tests:
#    pytest -m my_smoke_test_suite
# To run only one positive test:
#    pytest -m my_alway_green_tests
#

import pytest


@pytest.mark.my_smoke_test_suite
@pytest.mark.my_alway_green_tests
def test_simple01():
    """ To run only this test you should run the following command:

        pytest -m my_alway_green_tests

    """

    assert True


@pytest.mark.my_smoke_test_suite
@pytest.mark.my_alway_red_tests
def test_simple02():
    """ To run only this test you should run the following command:

        pytest -m my_alway_red_tests

    """

    assert False


@pytest.mark.my_smoke_test_suite
def test_simple03():
    """ To run this test:

        pytest -m my_smoke_test_suite

    """

    assert True
