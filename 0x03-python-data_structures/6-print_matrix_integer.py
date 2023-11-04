#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, value in enumerate(i):
            if j == 2:
                print("{}".format(value), end="")
            else:
                print("{}".format(value), end=" ")

        print()
