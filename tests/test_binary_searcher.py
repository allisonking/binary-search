import sys
import pytest
import random
sys.path.insert(0, 'binary_search')
from binary_searcher import BinarySearcher


@pytest.fixture
def simple_sorted_array():
    """Returns a sorted array with 10 values 0 through 9"""
    return list(range(10))


@pytest.fixture
def binary_searcher():
    """Returns a BinarySearcher instance"""
    return BinarySearcher()


@pytest.fixture
def array_of_one():
    """Returns an array with only the number 5 ([5])"""
    return [5]


@pytest.fixture
def odd_array():
    """Returns a randomly sorted array with 11 values"""
    return make_random_sorted_array(11)


@pytest.fixture
def even_array():
    """Returns a randomly sorted array with 20 values"""
    return make_random_sorted_array(20)


def make_random_sorted_array(num):
    """Helper method that makes a random sorted array of size num"""
    array = [random.randint(-1000, 1000) for _ in range(num)]
    return sorted(array)


def test_finding_first_value(simple_sorted_array, binary_searcher):
    assert binary_searcher.find(simple_sorted_array, 0) == 0


def test_finding_last_value(simple_sorted_array, binary_searcher):
    assert binary_searcher.find(simple_sorted_array, 9) == 9


def test_finding_all_values(simple_sorted_array, binary_searcher):
    for value in simple_sorted_array:
        assert binary_searcher.find(simple_sorted_array, value) == value


def test_return_negative_one_for_value_not_in_array(simple_sorted_array, binary_searcher):
    assert binary_searcher.find(simple_sorted_array, 50) == -1


def test_array_of_one(array_of_one, binary_searcher):
    assert binary_searcher.find(array_of_one, 5) == 0


def test_array_of_one_returns_negative_one_when_search_value_is_greater(array_of_one, binary_searcher):
    assert binary_searcher.find(array_of_one, 10000) == -1


def test_array_of_one_returns_negative_one_when_search_value_is_less(array_of_one, binary_searcher):
    assert binary_searcher.find(array_of_one, 2) == -1


def test_can_find_value_in_random_even_array(even_array, binary_searcher):
    index = random.randint(0, len(even_array)-1)
    value = even_array[index]
    assert binary_searcher.find(even_array, value) == index


def test_can_find_value_in_random_odd_array(odd_array, binary_searcher):
    index = random.randint(0, len(odd_array) - 1)
    value = odd_array[index]
    assert binary_searcher.find(odd_array, value) == index


def test_all_values_in_random_even_array(even_array, binary_searcher):
    for index, value in enumerate(even_array):
        assert binary_searcher.find(even_array, value) == index


# Just an example of parametrize
@pytest.mark.parametrize("array, value, expected", [
    ([4, 5, 6], 5, 1),
    ([-15, -14, 0, 2], -15, 0),
    ([50, 1000, 2345, 7890], 7890, 3)
])
def test_some_hard_coded_arrays(array, value, expected, binary_searcher):
    assert binary_searcher.find(array, value) == expected

