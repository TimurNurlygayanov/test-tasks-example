#!/usr/bin/env python3

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, FileType, ArgumentTypeError
from io import TextIOWrapper
from typing import List
import struct
import sys
import time


DEFAULT_DATASET_PATH = 'wikipedia_sample.txt'
DEFAULT_INVERTED_INDEX_PATH = 'inverted.index'


class InvertedIndex:
    index_data = {}

    def query(self, words: List) -> List:
        """Return the list of relevant documents for the given query"""
        # FIX ME
        results = set()

        for word in words:
            if results:
                results = results.intersection(set(self.index_data.get(word, set())))
            else:
                results = set(self.index_data.get(word, set()))

        return results

    def build(self, data_file='wikipedia_sample.txt', encoding='utf-8'):
        with open(data_file, 'r', encoding=encoding) as data_f:
            for line in data_f:
                text = line.split()

                # TODO: do we want to remove special characters here?
                # TODO: do we want to lowercase words?

                for word in set(text[1:]):
                    self.index_data.setdefault(word, []).append(int(text[0]))

        print(self.index_data)

    def dump(self, filepath: str):
        with open(filepath, 'wb') as inverted_index:
            # Write length of dict
            d = struct.pack('I', len(self.index_data))
            inverted_index.write(d)

            for word, numbers in self.index_data.items():
                # Write length of word
                w_length = len(word.encode())
                key_len = struct.pack('>H', w_length)
                inverted_index.write(key_len)


                # Write packed word
                bt_word = word.encode()
                # bt_word_packed = struct.pack('>{0}s'.format(w_length), bt_word)
                inverted_index.write(bt_word)


                # Write length of values list
                val_len = struct.pack('>H', len(numbers))
                inverted_index.write(val_len)

                # Write each element of list
                for doc_id in numbers:
                    doc_id_packed = struct.pack('>h', doc_id)
                    inverted_index.write(doc_id_packed)

    def load(self, filepath: str):
        self.index_data = {}

        with open(filepath, 'rb') as inverted_index:
            # get index_data length
            inv_index_len = struct.unpack('I', inverted_index.read(4))[0]

            for i in range(inv_index_len):
                # get word
                d_word_len = inverted_index.read(2)
                word_len = struct.unpack('>H', d_word_len)[0]
                d_word = inverted_index.read(word_len)
                print(d_word_len, word_len, d_word)
                # word = struct.unpack('>' + str(word_len) + 's', d_word)[0].decode()
                word = d_word.decode()

                # get list of values
                d_val_len = inverted_index.read(2)
                val_len = struct.unpack('>h', d_val_len)[0]
                d_values = inverted_index.read(2 * val_len)
                values = struct.unpack('>' + str(val_len) + 'h', d_values)

                self.index_data[word] = list(values)


def setup_parser(parser):
    subparsers = parser.add_subparsers(help='choose command')

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
        '--query-file-utf8', dest='query_file',
        default=TextIOWrapper(sys.stdin.buffer, encoding='utf-8'),
        help='path to query file in utf8 to load',
    )

    query_file_group.add_argument(
        '--query-file-cp1251', dest='query_file',
        default=TextIOWrapper(sys.stdin.buffer, encoding='cp1251'),
        help='path to query file in cp1251 to load',
    )

    query_file_group.add_argument(
        '--query', dest='query', nargs='+', action='append',
        default=[], help='query to search in inverted index',
    )


if __name__ == "__main__":
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

        manual_query = [q[0] for q in arguments.query]
        print(manual_query)
        if manual_query:
            results = inverted_index.query(manual_query)
            print(','.join([str(r) for r in results]))
            print(len(results))
