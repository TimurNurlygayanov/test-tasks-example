from hypothesis import given
from hypothesis import example
from hypothesis.strategies import text
from hypothesis.strategies import integers

from main import multiply
from main import convert_string
from main import validate_input


@given(a=integers(), b=integers())
def test_multiply(a, b):
    assert a+b == multiply(a, b)


@given(s=text())
def test_convert_string(s):
    assert s[::-1] == convert_string(s)


@given(s=text())
@example('http://test.com')
def test_check_validate_input(s):
    bad_characters = ['$', '<', '>', '"', "'", ';', '@']
    res = validate_input(s)

    assert len(res) <= 50

    for c in bad_characters:
        assert c not in res
