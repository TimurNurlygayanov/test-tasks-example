#!/usr/bin/env python3

""" Smoke unit tests for Index. """

import argparse
from unittest.mock import patch, mock_open

from inverted_index import InvertedIndex
from inverted_index import main


DATASET_TEST_SAMPLE = 'my.index'
DATASET_WIKIPEDIA_SAMPLE = 'data.txt'
QUERIES_UTF8_PATH = 'q.txt'

LONG_STRING = '''10 rrt DFNGVJHMGNFDFS DGDF DGDFG
12  This is tricky?
100500  Try this one also :)
'''

LONG_STRING_REPEATS = '''10 test this long string
1   this long string can be tricky?
100500  of course this long string is tricky!
'''

BINARY_DATA = (b'\x03\x00\x00\x00\x00\x02me\x00\x01\x00\x01\x00\x04'
               b'test\x00\x02\x00\x01\x00\x02\x00\x03you\x00\x01\x00\x02')


@patch('builtins.open', new_callable=mock_open,
       read_data='1    test    me first')
def test_build_index(mock_file):
    """ Check if we can build index from simple string. """

    my_index = InvertedIndex()
    my_index.build(mock_file)

    assert my_index.index_data == {'test': [1], 'me': [1], 'first': [1]}


@patch('builtins.open', new_callable=mock_open,
       read_data='1    test  test  me first')
def test_build_index2(mock_file):
    """ Check if we can build index from string with repeated word. """

    my_index = InvertedIndex()
    my_index.build(mock_file)

    assert my_index.index_data == {'test': [1], 'me': [1], 'first': [1]}


@patch('builtins.open', new_callable=mock_open,
       read_data='1    test  test,  me first')
def test_build_index3(mock_file):
    """ Check if we can build index from string with special characters. """

    my_index = InvertedIndex()
    my_index.build(mock_file)

    assert my_index.index_data == {'test': [1], 'test,': [1], 'me': [1], 'first': [1]}


@patch('builtins.open', new_callable=mock_open,
       read_data=LONG_STRING)
def test_build_index4(mock_file):
    """ Check if we can build index from file with several lines. """
    my_index = InvertedIndex()
    my_index.build(mock_file)

    # Check the index
    assert len(my_index.index_data) == 12
    assert len(my_index.index_data.values()) == 12


@patch('builtins.open', new_callable=mock_open,
       read_data='1    test    me first')
def test_dump_index(mock_file):
    """ Check if we can dump index. """

    my_index = InvertedIndex()
    my_index.build(mock_file)
    my_index.dump('my_Test.index')

    expected_calls = ["call('my_Test.index', 'wb')",
                      "call().write(b'\\x03\\x00\\x00\\x00')",
                      "call().write(b'\\x00\\x02')",
                      "call().write(b'me')",
                      "call().write(b'\\x00\\x01')",
                      "call().write(b'\\x00\\x04')",
                      "call().write(b'test')",
                      "call().write(b'\\x00\\x05')",
                      "call().write(b'first')"]

    all_calls = [str(call) for call in mock_file.mock_calls]

    for call in expected_calls:
        assert call in all_calls


@patch('builtins.open', new_callable=mock_open,
       read_data=BINARY_DATA)
def test_load_index(mock_file):
    """ Check if we can load index. """

    my_index = InvertedIndex()
    my_index.load('my_Test.index')

    assert my_index.index_data == {'me': [1],
                                   'test': [1, 2],
                                   'you': [2]}
    assert len(mock_file.mock_calls) > 1


@patch('builtins.open', new_callable=mock_open,
       read_data='1    test    me first')
def test_query(mock_file):
    """ Check if we can query some correct words. """

    my_index = InvertedIndex()
    my_index.build(mock_file)

    assert my_index.query(['test']) == {1, }


@patch('builtins.open', new_callable=mock_open,
       read_data=LONG_STRING_REPEATS)
def test_query2(mock_file):
    """ Check if we can query some correct words with repeats. """

    my_index = InvertedIndex()
    my_index.build(mock_file)

    assert my_index.query(['string', 'long']) == {1, 10, 100500}


@patch('builtins.open', new_callable=mock_open, read_data=BINARY_DATA)
def test_query_from_loaded(mock_file):
    """ Check if we can query after we load the index. """

    my_index = InvertedIndex()
    my_index.load('test.index')

    assert my_index.query(['me', 'test']) == {1, }
    assert len(mock_file.mock_calls) > 1


@patch('builtins.open', new_callable=mock_open, read_data=BINARY_DATA)
def test_query_from_loaded2(mock_file):
    """ Check if we can query some non-existed words. """

    my_index = InvertedIndex()
    my_index.load('test.index')

    assert my_index.query(['me', 'test', 'non existed']) == set()
    assert len(mock_file.mock_calls) > 1


@patch('argparse.ArgumentParser.parse_args',
       return_value=argparse.Namespace(parser='build',
                                       dataset_path='data.txt',
                                       inverted_index_path='my.idx'))
@patch('builtins.open', new_callable=mock_open, read_data=BINARY_DATA)
def test_build_args(mock_args, mock_file):
    """ Check args with build command. """

    main()
    assert len(mock_file.mock_calls) >= 1


@patch('argparse.ArgumentParser.parse_args',
       return_value=argparse.Namespace(parser='query', query='me',
                                       inverted_index_filepath='my.idx'))
@patch('builtins.open', new_callable=mock_open, read_data=BINARY_DATA)
def test_query_args(mock_args, mock_file):
    """ Check args with build command. """

    main()
    assert len(mock_file.mock_calls) >= 1
