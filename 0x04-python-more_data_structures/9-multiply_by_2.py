#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    key = [k for k, v in new_dic.items()]
    value = [v * 2 for k, v in new_dic.items()]
    return(dict(zip(key, value)))
