from functools import wraps


def check_array_type(func):
    """ Decorator that checks if an input is an array of numbers

    :param func: a function that expects an array as its first argument
    :return: raises an exception if the input is not an array of numbers, or returns True if it is
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg = args[0]
        if not isinstance(arg, list):
            raise TypeError('Please provide a list as input.')
        if all(isinstance(item, int) or isinstance(item, float) for item in arg):
            return func(*args, **kwargs)
        else:
            raise TypeError('Please provide a list of all numbers')
    return wrapper


@check_array_type
def binary_search(array, value):
    """Performs a binary search to find the index of a value in an array

     :param array: a sorted array of numbers
     :param value: a number to look for in the array
     :return: the first index (int) where the array equals the value, or -1 if the value is not in the array
     """
    low = 0
    high = len(array)-1
    while high >= low:
        mid = (low + high) // 2
        if value == array[mid]:
            return get_first_index(array, mid, value)
        elif value < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def get_first_index(array, index, value):
    """ Helper function to find the first instance of a value once it is found in binary search
    
    :param array: a sorted array of numbers
    :param index: the index of which an instance of the value was found
    :param value: the value we are looking for
    :return: the first index that a value appears in an array
    """
    if index > 0 and array[index-1] == value:
        return get_first_index(array, index-1, value)
    return index
