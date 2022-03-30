
def print_join(*lists, seperator='-'):
    """
    uncation that add the seperator for each list
    :param lists:
    :param seperator:
    :return:
    """
    list_with = [place for curr_list in lists for place in curr_list + [seperator]][:-1]
    if not list_with:
        return ()
    return list_with


if __name__ == '__main__':
    print(print_join([1, 2], [8], [9, 5, 6], seperator='@'))
