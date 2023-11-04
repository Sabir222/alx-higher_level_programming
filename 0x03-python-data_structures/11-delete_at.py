#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    new_list = []
    for index, value in enumerate(my_list):
        if index != idx:
            new_list.append(value)
    return new_list
