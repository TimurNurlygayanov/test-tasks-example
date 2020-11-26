from argparse import Namespace

import pytest

from task_salikhov_robert_inverted_index import (
    load_documents, process_queries,
    callback_query, DEFAULT_INVERTED_INDEX_PATH,
    process_build,
)

DATASET_TEST_SAMPLE = 'test_sample.txt'
DATASET_WIKIPEDIA_SAMPLE = 'wikipedia_sample.txt'
QUERIES_UTF8_PATH = 'queries_utf8.txt'


@pytest.mark.slow
@pytest.mark.parametrize(
    'dataset_path',
    [
        DATASET_TEST_SAMPLE,
        pytest.param(DATASET_WIKIPEDIA_SAMPLE, marks=[pytest.mark.slow]),
    ]
)
def test_process_build_can_load_documents(dataset_path):
    process_build(dataset_path, 'inverted.index')


def test_callback_query_can_process_all_queries_from_correct_file():
    with open(QUERIES_UTF8_PATH) as queries_fin:
        query_arguments = Namespace(
            inverted_index_filepath=DEFAULT_INVERTED_INDEX_PATH,
            query_file=queries_fin,
        )
        callback_query(query_arguments)
        assert 1 == 0


def test_process_queries_can_process_all_queries_from_correct_file(capsys):
    with open(QUERIES_UTF8_PATH) as queries_fin:
        process_queries(
            inverted_index_filepath=DEFAULT_INVERTED_INDEX_PATH,
            query_file=queries_fin,
        )
        captured = capsys.readouterr()
        assert 'load inverted index' not in captured.out
        assert 'load inverted index' in captured.err
        assert 'Anarchism' in captured.out
        assert 'Anarchism' not in captured.err
        assert 1 == 0


def test_load_documents_can_load_documents():
    etalon_documents = {
        '12': 'Anarchism Anarchism is often defined as a',
    }
    documents = load_documents(DATASET_TEST_SAMPLE)
    assert etalon_documents == documents, (
        'expected words and parsed words are not the same'
    )


# @pytest.mark.skip
def test_load_documents_can_load_wikipedia_sample():
    documents = load_documents(DATASET_WIKIPEDIA_SAMPLE)
    assert len(documents) == 4100, (
        'you correctly loaded Wikipedia dataset'
    )


# def test_get_words_raise_raise_exception_for_none():
#     with pytest.raises(AttributeError):
#         get_words(None)
