import sys
import pytest
import random
sys.path.insert(0, 'binary_search')
from binary_searcher import check_array_type, binary_search


@pytest.fixture
def simple_sorted_array():
    """Returns a sorted array with 10 values 0 through 9"""
    return list(range(10))


@pytest.fixture
def array_of_one():
    """Returns an array with only the number 5 ([5])"""
    return [5]


@pytest.fixture
def odd_array():
    """Returns a sorted array with 11 random values"""
    return make_random_sorted_array(11)


@pytest.fixture
def even_array():
    """Returns a sorted array with 20 random values"""
    return make_random_sorted_array(20)


@pytest.fixture
def array_of_duplicates():
    """Returns an array that contains duplicate values"""
    return [1, 2, 3, 3, 4, 5]


def make_random_sorted_array(num):
    """Helper method that makes a random sorted array of size num"""
    # array = [random.randint(-1000, 1000) for _ in range(num)]
    array = random.sample(range(-1000, 1000), num)
    return sorted(array)


def test_array_of_one(array_of_one):
    assert binary_search(array_of_one, 5) == 0


def test_array_of_one_returns_negative_one_when_search_value_is_greater(array_of_one):
    assert binary_search(array_of_one, 10000) == -1


def test_array_of_one_returns_negative_one_when_search_value_is_less(array_of_one):
    assert binary_search(array_of_one, 2) == -1


def test_can_find_value_in_random_even_array(even_array):
    index = random.randint(0, len(even_array)-1)
    value = even_array[index]
    assert binary_search(even_array, value) == index


def test_can_find_value_in_random_odd_array(odd_array):
    index = random.randint(0, len(odd_array) - 1)
    value = odd_array[index]
    assert binary_search(odd_array, value) == index


def test_all_values_in_random_even_array(even_array):
    for index, value in enumerate(even_array):
        assert binary_search(even_array, value) == index


def test_values_outside_range(even_array):
    assert binary_search(even_array, even_array[0]-1) == -1
    assert binary_search(even_array, even_array[len(even_array)-1] + 1) == -1


# Just an example of parametrize
@pytest.mark.parametrize("array, value, expected", [
    ([4, 5, 5, 6], 5, 1),
    ([5, 5, 5, 5], 5, 0),
    ([4, 5, 5, 5, 6, 7, 8], 5, 1),
    ([50, 1000, 2345, 2345], 2345, 2),
    ([50, 1000, 1001, 1002, 2345, 2345, 2345], 2345, 4)
])
def test_can_find_duplicates(array, value, expected):
    assert binary_search(array, value) == expected


# Now test type checking
@pytest.mark.parametrize("arg", [
    5,
    'some word',
    ['array', 'of', 'strings']
])
def test_bad_types(arg):
    with pytest.raises(TypeError):
        binary_search(arg, 'random')


@pytest.mark.parametrize("arg, value, expected", [
    ([1, 2, 3, 4], 2, 1),
    ([-10, -2.3, -1.2], -1.2, 2),
    ([4.33234], 0, -1)
])
def test_good_types(arg, value, expected):
    assert binary_search(arg, value) == expected


