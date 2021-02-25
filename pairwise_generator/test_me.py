import pytest
from allpairspy import AllPairs


def is_valid_combination(row):
    """ This function allows to control that we are using
        only the correct combinations in tests.
    """

    if len(row) > 1:
        if 'Brand X' == row[0] and row[1] == '2000':
            return False

    return True


def function_to_be_tested(brand, operating_system, minute):
    # Just return True to pass all tests
    return True


@pytest.mark.parametrize(['brand', 'operating_system', 'minute'], [
    value_list for value_list in AllPairs([
        ['Brand X', 'Brand Y'],
        ['98', 'NT', '2000', 'XP'],
        [10, 15, 30, 60]
    ], filter_func=is_valid_combination)
])
def test(brand, operating_system, minute):
    assert function_to_be_tested(brand, operating_system, minute)
