#!/usr/bin/python3
for number in range(0, 100):
    formatted = f"{number:02}"
    if number != 99:
        print("{}, ".format(formatted), end="")
    else:
        print("{}".format(formatted))
