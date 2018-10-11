

def my_decorator_empty(f):
    """ This is decorator function.
        Argument f is a function.
    """

    def decorator_magic(*args, **kwargs):
        f(*args, **kwargs)

    return decorator_magic


def my_decorator_with_magic(f):
    """ This is decorator function.
        Argument f is a function.
    """

    def decorator_magic(*args, **kwargs):
        print("Before function !!!")
        f(*args, **kwargs)
        print("After function  !!!")

    return decorator_magic


@my_decorator_empty
def my_func(a, b):
    print("a: {0}, b: {1}".format(a, b))


@my_decorator_with_magic
def my_func2(a, b):
    print("a: {0}, b: {1}".format(a, b))


my_func(1, 2)

my_func2(3, 4)
