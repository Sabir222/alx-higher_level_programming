#!/usr/bin/python3


def uppercase(str):
    result = ""
    for i in str:
        if i == " ":
            result += " "
        elif ord("a") <= ord(i) <= ord("z"):
            result += chr(ord(i) - 32)
        else:
            result += i
    print(result)
