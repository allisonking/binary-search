class BinarySearcher:
    """A class that can find values in an array using a binary search"""

    @staticmethod
    def find(array, value):
        """Performs a binary search to find the index of a value in an array
         
        Arguments:
            array- a sorted array of numbers
            value- a number to look for in the array
         
        Returns:
            the index (int) where the array equals the value, or -1 if the value is not in the array
        """

        # these are the cases where the value is not found in the array
        if len(array) == 0 or (len(array) == 1 and array[0] != value):
            return -1

        # find the half way point of the array
        halfway_index = int(round(len(array)/2))

        # see if the halfway value is the value we want
        if value == array[halfway_index]:
            return halfway_index

        # otherwise, check if value might be in first half and recurse with first half of the array
        elif value < array[halfway_index]:
            return BinarySearcher.find(array[:halfway_index], value)

        # if not, value might be greater, so recurse with second half of the array
        else:
            ret_val = BinarySearcher.find(array[halfway_index:], value)
            # if the value was not found, just pass -1 back up
            if ret_val < 0:
                return ret_val
            # otherwise, add the halfway index since we had split at this index earlier
            return halfway_index + ret_val
