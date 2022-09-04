def swap_pair(lst, i, j):
    '''
    Function swaps two items in a list
    '''
    lst[i], lst[j] = lst[j], lst[i]


def shift_pair(lst, i, limit):
    '''
    Function creates heap from items in a list, with given limit
    :param lst: list of tuples (key:value pair) created from dictionary
    :param limit: length of the list
    :return: True
    '''
    while True:
        l, r = i*2+1, i*2+2
        if max(l, r) < limit:
            if lst[i][1] >= max(lst[l][1], lst[r][1]):
                break
            elif lst[l][1] > lst[r][1]:
                swap_pair(lst, i, l)
                i = l
            else:
                swap_pair(lst, i, r)
                i = r
        elif l < limit:
            if lst[l][1] > lst[i][1]:
                swap_pair(lst, i, l)
                i = l
            else:
                break
        elif r < limit:
            if lst[r][1] > lst[i][1]:
                swap_pair(lst, i, r)
                i = r
            else:
                break
        else:
            break
    return True


def dictionary_heapsort(lst):
    '''
    Heapsort of a given dictionary
    :param lst:
    :return: list of tuples (key:value pairs)
    '''
    lst = list(lst.items())
    for j in range((len(lst)-2)//2, -1, -1):
        shift_pair(lst, j, len(lst))

    for end in range(len(lst)-1, 0, -1):
        swap_pair(lst, 0, end)
        shift_pair(lst, 0, end)
    return lst


def sorted_dict_keys(dictionary):
    '''
    Extracts sorted keys based on values from given dictionary
    :param dictionary:
    :return: list of sorted keys
    '''
    sorted_dict = dictionary_heapsort(dictionary)
    return [key[0] for key in sorted_dict]


element = {"a": 1, "b": 5, "c": 8, "d": 5, "e": 12, "f": 3, "g": 43, "h": 6}


if __name__ == "__main__":
    print(dictionary_heapsort(element))
    print(sorted_dict_keys(element))
