#!/usr/bin/python3
# -*- encoding=utf8 -*-

# How To Run:
#     pytest -vv test_pytest_parametrized_tests.py
#

import pytest


@pytest.mark.parametrize('a', ['test', 1])
@pytest.mark.parametrize('b', ['test', 2])
def test_with_some_parameters(a, b):
    """ This is very simple example of test with parameters.
        It will be executed 4 times with the following parameters:

         1) a = 'test', b = 'test'
         2) a = 'test', b = 2
         3) a = 1, b = 'test'
         4) a = 1, b = 2

        So, this test will fail only once :)

    """

    assert a != b, 'a == b - it is very bad!'
