#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    while search in new_list:
        idx = new_list.index(search)
        new_list[idx] = replace
    return new_list
