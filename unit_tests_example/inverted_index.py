#!/usr/bin/env python3

""" Basic Reverse Index implementation. """

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from typing import List
import struct
import sys


DEFAULT_DATASET_PATH = 'wikipedia_sample.txt'
DEFAULT_INVERTED_INDEX_PATH = 'inverted.index'


class InvertedIndex:
    """ Index class. """

    index_data = None

    def __init__(self):
        self.index_data = {}

    def query(self, words: List) -> List:
        """ Return the list of relevant documents for the given query. """

        q_results = set()

        for word in words:
            if q_results:
                # Get only equal elements from two different sets of indexes
                q_results = q_results.intersection(set(self.index_data.get(word, set())))
            else:
                q_results = set(self.index_data.get(word, set()))

        return q_results

    def build(self, data_file='wikipedia_sample.txt', file_encoding='utf-8'):
        """ Build index in RAM. """

        with open(data_file, 'r', encoding=file_encoding) as data_f:
            for short_line in data_f:
                text = short_line.split()

                for word in set(text[1:]):
                    self.index_data.setdefault(word, []).append(int(text[0]))

    def dump(self, filepath: str):
        """ Save index to file. """

        with open(filepath, 'wb') as inverted_index_file:
            # Write length of dict
            dict_length = struct.pack('I', len(self.index_data))
            inverted_index_file.write(dict_length)

            for word, numbers in self.index_data.items():
                # Write length of word
                w_length = len(word.encode())
                key_len = struct.pack('>H', w_length)
                inverted_index_file.write(key_len)

                # Write packed word
                bt_word = word.encode()
                inverted_index_file.write(bt_word)

                # Write length of values list
                val_len = struct.pack('>H', len(numbers))
                inverted_index_file.write(val_len)

                # Write each element of list
                for doc_id in numbers:
                    doc_id_packed = struct.pack('>H', doc_id)
                    inverted_index_file.write(doc_id_packed)

    def load(self, filepath: str):
        """ Load index from file. """

        self.index_data = {}

        with open(filepath, 'rb') as inverted_index_file:
            # get index_data length
            inv_index_len = struct.unpack('I', inverted_index_file.read(4))[0]

            for _ in range(inv_index_len):
                # get word
                d_word_len = inverted_index_file.read(2)
                word_len = struct.unpack('>H', d_word_len)[0]
                d_word = inverted_index_file.read(word_len)
                word = d_word.decode()

                # get list of values
                d_val_len = inverted_index_file.read(2)
                val_len = struct.unpack('>H', d_val_len)[0]
                d_values = inverted_index_file.read(2 * val_len)
                values = struct.unpack('>' + str(val_len) + 'H', d_values)

                self.index_data[word] = list(values)


def setup_parser(my_parser):
    """ Parser for command line arguments. """

    subparsers = my_parser.add_subparsers(help='choose command')

    build_parser = subparsers.add_parser(
        'build',
        help='build inverted index and save in binary format into hard drive',
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    build_parser.set_defaults(parser='build')

    build_parser.add_argument(
        '--dataset',
        dest='dataset_path',
        default=DEFAULT_DATASET_PATH,
        help='path to dataset to load',
    )

    build_parser.add_argument(
        '--output',
        dest='inverted_index_path',
        default=DEFAULT_INVERTED_INDEX_PATH,
        help='path to save inverted index in a binary format',
    )

    query_parser = subparsers.add_parser(
        'query',
        help='query in inverted index',
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    query_parser.set_defaults(parser='query')

    query_parser.add_argument(
        '--index',
        dest='inverted_index_filepath',
        default=DEFAULT_INVERTED_INDEX_PATH,
        help='path to inverted index in binary format to load',
    )

    query_file_group = query_parser.add_mutually_exclusive_group(required=True)

    query_file_group.add_argument(
        '--query-file-utf8', dest='query_file_utf8',
        default='',
        help='path to query file in utf8 to load',
    )

    query_file_group.add_argument(
        '--query-file-cp1251', dest='query_file_cp1251',
        default='',
        help='path to query file in cp1251 to load',
    )

    query_file_group.add_argument(
        '--query', dest='query', nargs='+', action='append',
        default=[], help='query to search in inverted index',
    )


def main():
    """ Starting point for the script. """

    parser = ArgumentParser(
        prog='inverted-index',
        description='tool to build, dump, load and query inverted index',
    )
    setup_parser(parser)
    arguments = parser.parse_args()

    inverted_index = InvertedIndex()

    if arguments.parser == 'build':
        inverted_index.build(data_file=arguments.dataset_path)
        inverted_index.dump(filepath=arguments.inverted_index_path)

    elif arguments.parser == 'query':
        inverted_index.load(filepath=arguments.inverted_index_filepath)

        queries = []
        for q in arguments.query:
            queries.append(' '.join([z for z in q]))

        if not queries or not queries[0]:
            query_file = ''
            encoding = 'utf-8'

            if arguments.query_file_utf8 == '-':
                query_file = '-'
            elif len(arguments.query_file_utf8) > 2:
                query_file = arguments.query_file_utf8
            elif arguments.query_file_cp1251 == '-':
                query_file = '-'
            elif len(arguments.query_file_cp1251) > 2:
                query_file = arguments.query_file_cp1251
                encoding = 'cp1251'

            if query_file == '-':
                # Read from stdin:
                data = sys.stdin.read()
                queries = [q for q in data.split('\n') if q]
            else:
                with open(query_file, 'r', encoding=encoding) as q_file:
                    queries = []
                    for line in q_file.readlines():
                        queries.append(' '.join([q for q in line.split() if q]))

        for query_string in queries:
            results = inverted_index.query(query_string.split())
            print(','.join([str(r) for r in results]))


if __name__ == "__main__":
    main()
