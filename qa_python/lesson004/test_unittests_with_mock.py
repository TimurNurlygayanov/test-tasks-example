#!/usr/bin/python3
# -*- encoding=utf8 -*-

# More information:
#   https://docs.python.org/3/library/unittest.mock.html
#
# How to Run tests:
#    python3 -m venv env
#    source env/bin/activate
#    pip3 install -r requirements.txt
#    python3 -m nose -v test_unittests_with_mock.py
#

import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import mock_open

from product_example import MySuperProgram


class MyTests(unittest.TestCase):

    @patch('product_example.open', mock_open(read_data='test1\ntest3\ntest2\n'))
    def test_read_one_line_with_mock(self):
        """ Check read_string_from_file() function. """

        prog = MySuperProgram()
        str = prog.read_string_from_file()

        msg = 'Expected: "{0}" Actual: "{1}"'.format('test1\n', str)
        assert str == 'test1\n', msg

    @patch('product_example.open', mock_open(read_data='test1\ntest3\ntest2\n'))
    def test_read_all_lines_with_mock(self):
        """ Check read_and_sort_all_strings() function. """

        prog = MySuperProgram()
        all_strings = prog.read_and_sort_all_strings()

        assert all_strings == ['test1', 'test2', 'test3']


if __name__ == '__main__':
    unittest.main()
