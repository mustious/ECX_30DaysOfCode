def bin_search(ordered_list: list, item):
    """
    searches through a list of elements by repeatively subdiving it, which sublist the element falls on
    very effective when using an ordered set of elements

    :param ordered_list: list to be searched
    :param item: item to be found
    :return: boool
    """

    copy_list = ordered_list
    if len(copy_list) == 0:
        return False
    else:
        middle_index = len(copy_list) // 2

    if item == copy_list[middle_index]:
        return True
    elif item > copy_list[middle_index]:
        return bin_search(copy_list[middle_index+1:], item)
    else:
        return bin_search(copy_list[:middle_index], item)
