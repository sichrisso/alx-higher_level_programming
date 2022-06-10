#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_lists = set(my_list)
    sum = 0
    for i in new_lists:
        sum += i
    return sum
