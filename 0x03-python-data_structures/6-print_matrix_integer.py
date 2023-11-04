#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, value in enumerate(i):
            if j == 2:
                print("{}".format(j), end="")
            else:
                print("{}".format(j), end=" ")

        print()
