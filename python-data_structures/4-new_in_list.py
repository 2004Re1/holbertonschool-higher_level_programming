#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    my_list1 = my_list.copy()
    my_list1[idx] = element
    return my_list1
