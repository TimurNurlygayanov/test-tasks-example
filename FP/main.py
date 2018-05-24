# -*- encoding=utf8 -*-

import re


OKGREEN = '\033[92m\033[1m'
FAIL = '\033[91m\033[1m'
ENDC = '\033[0m'


# This is my own implementation of the function which should be tested:
def check_string(s):
    pattern = re.compile('[A-Za-zА-Яа-яЁёΑ-Ωα-ω0-9]{2}')
    return int( bool(pattern.match(s)) )


# This is the list of test cases, which should be passed:
TEST_CASES = [
    {'value': 'AA', 'expected_result': 1},
    {'value': '1A', 'expected_result': 1},
    {'value': '11', 'expected_result': 1},
    {'value': 'A$', 'expected_result': 0},
    {'value': '(1', 'expected_result': 0},

    # Test Scenarios to verify bug fix:

    {'value': 'РФ', 'expected_result': 1},  # Cyrilic capital characters
    {'value': 'аа', 'expected_result': 1},  # Cyrilic non-capital equal characters
    {'value': 'Ёж', 'expected_result': 1},  # Cyrilic capital + non-capital characters and
                                            # one of "non popular" Cyrilic character Ё
    {'value': 'ю1', 'expected_result': 1},  # Cyrilic character and number
    {'value': 'RЩ', 'expected_result': 1},  # Cyrilic and Latin characters
    {'value': 'я:', 'expected_result': 0},  # Cyrilic character and non-character symbol

    # New test cases:

    {'value': 'zF', 'expected_result': 1},  # Capital Latin catacter and non-capital latin character
    {'value': 'Ωω', 'expected_result': 1},  # Modern Greek capital and non-capital characters
    {'value': 'ζλ', 'expected_result': 1},  # Some Modern Greek non-capital characters
    {'value': 'Ξ0', 'expected_result': 1},  # Capital Modern Greek character and number
    {'value': 'ζЫ', 'expected_result': 1},  # Modern Greek and Cyrilic characters
    {'value': 'RΞ', 'expected_result': 1},  # Modern Greek and Latin characters
    {'value': '-5', 'expected_result': 0},  # Number and non-correct character
    {'value': '\w', 'expected_result': 0},  # Regexp pattern in input
    {'value': '→→', 'expected_result': 0},  # Some incorrect unicode symbols
    {'value': 'ϘϺ', 'expected_result': 0},  # Old Greek characters (not included in Modern Greek)
]


msg = 'Value: {0}, expected result: {1}, actual result: {2}, status: {3}'

# Run tests and print results:
for test in TEST_CASES:
    value = test['value']
    expected = test['expected_result']
    actual = check_string(value)
    status = OKGREEN + 'Passed' + ENDC if expected == actual else FAIL + 'Failed' + ENDC

    print(msg.format(value, expected, actual, status))
