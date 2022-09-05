ELEMENT = {"a": 6, "b": 5, "c": 8, "d": 5, "e": 12, "f": 3, "g": 43, "h": 1}


# Quicksort function - body

def partition(l, r, lst):
    """
    Sorts values smaller and greater than pivot value to left and right side of the pivot, accordingly.
    :param l: left boundary (initially 0)
    :param r: right boundary (initially last item of a dictionary)
    :param lst: list of items to part
    :return: pointer
    """
    pivot, pointer = lst[r][1], l
    for i in range(l, r):
        if lst[i][1] <= pivot:

            lst[i], lst[pointer] = lst[pointer], lst[i]
            pointer += 1

    lst[pointer], lst[r] = lst[r], lst[pointer]

    return pointer


def quicksort(l, r, lst):
    """
    Quicksort algorithm. Calls partition method and recursively quicksort parted fragments of the list.
    :param l: int (lower end of given list)
    :param r: int (higher end of given list)
    :param lst: list (list to sort)
    :return: list (sorted list)
    """

    if len(lst) == 1:
        return lst

    if l < r:
        pi = partition(l, r, lst)
        quicksort(l, pi - 1, lst)
        quicksort(pi + 1, r, lst)

    return lst


# Quicksort - dictionary conversion

def dictionary_quicksort(dictionary):
    """
    Transforms dictionary to list of tuples and using quicksort algorithm sorts items based on dictionary values.
    :param dictionary: dictionary
    :return: list of tuples
    """
    lst = list(dictionary.items())
    quicksort(0, len(lst) - 1, lst)
    return lst


def get_dict_keys_sorted_quicksort(dictionary):
    """
    Sorts dictionary by its values and returns sorted keys.
    :param dictionary: dictionary
    :return: list of tuples
    """
    return [key[0] for key in dictionary_quicksort(dictionary)]


if __name__ == '__main__':
    print(dictionary_quicksort(ELEMENT))
    print(get_dict_keys_sorted_quicksort(ELEMENT))
