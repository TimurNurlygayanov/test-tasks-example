#!/usr/bin/python3
# -*- encoding=utf8 -*-

# More information:
#   https://docs.python.org/3/library/unittest.mock.html
#

import unittest
from unittest.mock import MagicMock
from unittest.mock import patch


@patch('open', MagicMock())
def test_with_mock(self):
    f = open('test')
    print(type(f))
