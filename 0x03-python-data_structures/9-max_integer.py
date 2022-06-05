def max_integer(my_list=[]):
    if my_list and len(my_list) > 0:
        return sorted(my_list)[-1]
    else:
        return None
