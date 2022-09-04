def partition(l, r, lst):
    """

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

    if len(lst) == 1:
        return lst

    if l < r:
        pi = partition(l, r, lst)
        quicksort(l, pi - 1, lst)
        quicksort(pi + 1, r, lst)

    return lst


def dict_quicksort(dictionary):
    lst = list(dictionary.items())
    quicksort(0, len(lst) - 1, lst)
    return lst


def get_dict_keys_sorted(dictionary):
    return [key[0] for key in dict_quicksort(dictionary)]


element = {"a": 1, "b": 5, "c": 8, "d": 5, "e": 12, "f": 3, "g": 43, "h": 6}

if __name__ == '__main__':
    print(dict_quicksort(element))
    print(get_dict_keys_sorted(element))
