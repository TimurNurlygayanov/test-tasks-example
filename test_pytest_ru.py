#!/usr/bin/python3
# -*- encoding=utf8 -*-
# encoding: utf-8

import pytest


@pytest.mark.parametrize('a', [u"к"])
def test_my_ru_test(a):
    assert a > ''
