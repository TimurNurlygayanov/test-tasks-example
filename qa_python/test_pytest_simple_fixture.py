#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is the very simple example of PyTest fixture for tests.
#
# Note: PyTest also has many default "buildin" fixtures
#
# More info: https://docs.pytest.org/en/latest/fixture.html
#

import pytest
from random import random_int


# Each fixture should have this decorator '@pytest.fixture'
@pytest.fixture
def number_fixture():
    """ This is simple fixture which return random int. """

    return random_int(10)


def test_check_random_number(number_fixture):
    """ This is example of simple test which uses simple fixture.

        Note: this test case has parameter - the name of parameter
              is equal to the name of function with '@pytest.fixture'
              decorator. PyTest will pass the result of function
              'def number_fixture()' as a parameter for the test case.

    """

    assert number_fixture > 5, 'Random number not bigger than 5!'
