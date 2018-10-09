# This is a simple example of fixture with parameters
# Note: need to specify indirect=True
#
# How to run:
#   pytest -s -v parametrized_fixture.py

import pytest


@pytest.fixture()
def my_fixture(request):
    my_params = request.param

    print('Fixture with params: {0}'.format(my_params))


@pytest.mark.parametrize('my_fixture', [{'a': 1, 'b': 2},
                                        {'a': 10, 'b': 15}], indirect=True)
def test_my_example_test(my_fixture):
    print('it is my test')
