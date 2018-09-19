#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is the very simple example of PyTest test case
# Note: the name of file with test cases should start
# with 'test_' - otherwice PyTest will not check this file
# for automated tests and will not run them.
#
# To run test cases, execute the following commands:
# cd qa_python
# pytest -v test_pytest_001.py
#


def test_which_should_always_fail():
    """ This is the test case. The name of each test case
        should start with 'test_' - otherwise PyTest will
        not run it.

        This test will always fail, it is just an example :)

    """

    expected = 0
    actual = 1

    assert expected == actual, 'Expected not equal to Actual!'


def test_which_should_always_pass():
    """ This is the test case. The name of each test case
        should start with 'test_' - otherwise PyTest will
        not run it.

        This test will always pass, it is just an example :)

    """

    expected = 0
    actual = 0

    assert expected == actual, 'Expected not equal to Actual!'
