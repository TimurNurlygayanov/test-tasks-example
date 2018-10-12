import pytest
import requests
from requests.auth import HTTPBasicAuth


user = 'test_user'
password = 'test_password'
host = 'http://0.0.0.0:7000'


@pytest.fixture(scope='function')
def auth_cookie():
    """ This fixture allows to get auth cookie. """

    url = '{0}/login'.format(host)
    result = requests.get(url,
                          auth=HTTPBasicAuth(user, password))
    data = result.json()

    # Return auth_cookie to test:
    yield data['auth_cookie']


def test_check_login():
    """ This test checks that login REST API works fine. """

    url = '{0}/login'.format(host)

    # Send GET REST API request with basic auth:
    result = requests.get(url,
                          auth=HTTPBasicAuth(user, password))
    data = result.json()

    # Verify that server returns some auth cookie:
    assert result.status_code == 200
    assert data['auth_cookie'] > ''


def test_check_list_of_books(auth_cookie):
    """ This test checks /books REST API function.  """

    url = '{0}/books'.format(host)
    result = requests.get(url, cookies={'my_cookie': auth_cookie})
    data = result.json()

    assert result.status_code == 200
    assert type(data) == list


def test_add_book(auth_cookie):
    """ Create new book and check that book was successfully created.

        Steps:
        1) Add new book
        2) Get list of all books
        3) Check that new book is presented in the list of all books

    """

    url = '{0}/add_book'.format(host)
    new_book = {'title': 'Book about QA', 'author': 'Me :)'}

    # Create new book:
    # Note: here we sending POST request with cookie and body!
    result = requests.post(url, data=new_book,
                           cookies={'my_cookie': auth_cookie})
    data = result.json()
    # Get id of created book:
    new_book['id'] = data['id']

    # Get list of books (GET request with cookie!):
    result2 = requests.get('http://0.0.0.0:7000/books',
                           cookies={'my_cookie': auth_cookie})
    all_books = result2.json()

    # Verify that new book is presented in the list of books:
    assert new_book in all_books


def test_delete_book(auth_cookie):
    """ Create new book, delete it and check that book was successfully deleted.

        Steps:
        1) Create new book
        2) Delete this book
        3) Get list of all books and verify that this book is not presented
           in the list

    """

    url = '{0}/add_book'.format(host)
    new_book = {'title': 'Book about QA', 'author': 'Me :)'}

    # Create new book:
    result = requests.post(url, data=new_book,
                           cookies={'my_cookie': auth_cookie})
    data = result.json()
    # Get id of created book:
    new_book['id'] = data['id']

    # Delete book (Note: DELETE REST API request with cookie!):
    url = '{0}/books/{1}'.format(host, new_book['id'])
    result = requests.delete(url,
                             cookies={'my_cookie': auth_cookie})

    # Get list of books:
    result = requests.get('{0}/books'.format(host),
                          cookies={'my_cookie': auth_cookie})
    list_of_all_books = result.json()

    # Verify that book is not presented in the list:
    assert new_book not in list_of_all_books
