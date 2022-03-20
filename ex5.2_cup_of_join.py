#funcation that add the seperator for each list
def print_join(*lists, seperator='-'):
    list_with= [cell for curr_list in lists for cell in curr_list + [seperator]][:-1]
    if list_with ==[]:
        return 'empty'
    return list_with

if __name__ == '__main__':
    print(print_join([1,2],[8],[9,5,6],seperator='@'))