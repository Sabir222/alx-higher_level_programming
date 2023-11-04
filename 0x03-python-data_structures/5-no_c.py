#!/usr/bin/python3


def no_c(my_string):
    newstrig = ""
    for i in my_string:
        if i != "c" and i != "C":
            newstrig += i
    return newstrig
