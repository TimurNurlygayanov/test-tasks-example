#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is simple example of decorator with parameters.

import functools
import timeit
import time


def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator!")
            if number == 13:
                print("Not running the function!")
            else:
                tic = timeit.default_timer()
                func(*args, **kwargs)
                toc = timeit.default_timer() - tic
                print('Total time for func is:', round(toc,8))
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator


@decorator_with_arguments(111)
def my_function(x, y):
    time.sleep(1)
    print(x+y)


my_function(87, 78)
