#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for number in matrix:
        l = 1
        for i in number:
            if l == len(i):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            l = l + 1
        print()


"""def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, value in enumerate(i):
            if j == 2:
                print("{:d}".format(value), end="")
            else:
                print("{:d}".format(value), end=" ")
        print()"""
