#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[y**2 for y in x] for x in matrix]


# def square_matrix_simple(matrix=[]):
#     squaredMatrix = []
#     for i in matrix:
#         row = [j**2 for j in i]
#         squaredMatrix.append(row)
#     return squaredMatrix
