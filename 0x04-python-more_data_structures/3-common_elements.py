#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for i in list(set_1):
        if i in list(set_2):
            new_list.append(i)
    return new_list
