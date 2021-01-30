s = ('eogmgdk352k4mkfldmklm342klmfldmlk342m34lkmf '
     'ekmrflk4324k rkmwer,ew.efwe24234.34234')


# solution #1
def my_func(my_str):
    my_digit = ''
    result = 0

    for s in my_str:
        if s.isnumeric():
            my_digit += s
        elif my_digit:
            result += int(my_digit)
            my_digit = ''

    if my_digit:
        result += int(my_digit)

    return result


# solution #2
import re


def my_func2(my_str):
    my_numbers = re.findall(r'[0-9]+', my_str)
    return sum([int(s) for s in my_numbers])


res = my_func(s)
print(res)

res = my_func2(s)
print(res)
