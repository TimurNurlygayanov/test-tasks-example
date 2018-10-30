#!/usr/bin/python3
# -*- encoding=utf8 -*-

# How to run the tests?
# 1) Install virtualenv:
#    python3 -m venv ./env
#    source ./env/bin/activate
#    pip install -r requirements.txt
# 2) Run tests:
#    nosetests -s qa_python/lesson003/unittests_example001.py
#

import unittest


class MyFirstTests(unittest.TestCase):

    test_me = []
    a = ''

    def setUp(self):
        print("Hi, I'm a function which will be executed before each test!")

    def tearDown(self):
        print("Hi, I'm a function which will be executed after each test!")

    @classmethod
    def setUpClass(cls):
        print("Hi, I'm a function which will be executed before "
              "all test suite - and only once!")

    @classmethod
    def tearDownClass(cls):
        print("Hi, I'm a function which will be executed after "
              "all test suite - and only once!")

    def test_my_first_test(self):
        print("This is my first test!")

    def test_my_second_test(self):
        print("This is my second test!")


if __name__ == '__main__':
    unittest.main()
