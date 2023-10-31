#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if i == " ":
            print("{}".format(" "), end="")
        elif ord("a") <= ord(i) <= ord("z"):
            print(chr(ord(i) - 32), end="")
        else:
            print("{}".format(i), end="")
