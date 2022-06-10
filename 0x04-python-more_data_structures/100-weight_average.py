#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        sum = 0
        divider = 0
        for tup in my_list:
            sum += tup[0] * tup[1]
            divider += tup[1]
        return (sum / divider) if divider > 0 else 0
    return (0)
