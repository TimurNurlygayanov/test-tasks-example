# Just simple example of decorators
#

from datetime import datetime
import requests


def timeit(parameter):
    def parameters_parser(func):
        def decorator(*args, **kwargs):
            print('Before function: ', parameter)

            start = datetime.now()

            result = func(*args, **kwargs)

            total = datetime.now() - start

            print('Finished in {0} seconds'.format(total.seconds))

            return result

        return decorator

    return parameters_parser


@timeit(parameter='test me')
def my_test_function():
    result = requests.get('https://reddit.com')

    print('Status code:', result.status_code)
    print('Content Size:', len(result.text))

    assert result.status_code == 200


# Run test
if __name__ == '__main__':
    my_test_function()
