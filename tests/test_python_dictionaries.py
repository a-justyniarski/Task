import pytest
import task_dictionary_quicksort, task_dictionary_heapsort


PARAMETERS = 'dictionary'
# Dictionaries: Already sorted, sorted reverse, with two values repeated n-times, duplicate of dictionary,
# dictionary with same value, duplicated keys with updated values. I do not check stability of sort algorithms.
DICTIONARY = (
    ({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}),
    ({"a": 6, "b": 5, "c": 8, "d": 5, "e": 6, "f": 5, "g": 43, "h": 1}),
    ({"a": 6, "b": 5, "c": 6, "d": 5, "e": 6, "f": 5, "g": 6, "h": 5}),
    ({"a": 8, "b": 7, "c": 6, "d": 5, "e": 4, "f": 3, "g": 2, "h": 1}),
    ({"a": 6, "b": 5, "c": 8, "d": 5, "e": 12, "f": 3, "g": 43, "h": 1}),
    ({"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1}),
    ({"a": 6, "b": 5, "c": 8, "d": 5, "e": 12, "f": 3, "g": 43, "h": 1,
      "a": 6, "b": 5, "c": 8, "d": 5, "e": 12, "f": 3, "g": 43, "h": 1}),
    ({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8,
      "a": 6, "b": 5, "c": 8, "d": 5, "e": 12, "f": 3, "g": 43, "h": 1}),
    ({}),
)


@pytest.mark.parametrize(PARAMETERS, DICTIONARY)
def test_dictionary_quicksort(dictionary):
    sorted_dict = task_dictionary_quicksort.dictionary_quicksort(dictionary)
    for idx, i in enumerate(sorted_dict):
        if idx+1 == len(sorted_dict):
            break
        assert dictionary[sorted_dict[idx][0]] <= dictionary[sorted_dict[idx+1][0]]


@pytest.mark.parametrize(PARAMETERS, DICTIONARY)
def test_get_dict_keys_sorted_quicksort(dictionary):
    sorted_dict = task_dictionary_quicksort.get_dict_keys_sorted_quicksort(dictionary)
    for idx, i in enumerate(sorted_dict):
        if idx+1 == len(sorted_dict):
            break
        assert dictionary[sorted_dict[idx]] <= dictionary[sorted_dict[idx+1]]


@pytest.mark.parametrize(PARAMETERS, DICTIONARY)
def test_dictionary_heapsort(dictionary):
    sorted_dict = task_dictionary_heapsort.dictionary_heapsort(dictionary)
    for idx, i in enumerate(sorted_dict):
        if idx+1 == len(sorted_dict):
            break
        assert dictionary[sorted_dict[idx][0]] <= dictionary[sorted_dict[idx+1][0]]


@pytest.mark.parametrize(PARAMETERS, DICTIONARY)
def test_get_dict_keys_sorted_heapsort(dictionary):
    sorted_dict = task_dictionary_heapsort.get_dict_keys_sorted_heapsort(dictionary)
    for idx, i in enumerate(sorted_dict):
        if idx+1 == len(sorted_dict):
            break
        assert dictionary[sorted_dict[idx]] <= dictionary[sorted_dict[idx+1]]


