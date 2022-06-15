#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == []:
        return None
    my_set = set(my_list)
    total = 0
    for item in my_set:
        total += item
    return total
