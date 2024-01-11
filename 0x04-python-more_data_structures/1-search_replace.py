#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = list(my_list)
        while search in new_list:
            new_list.remove(search)
        return new_list
