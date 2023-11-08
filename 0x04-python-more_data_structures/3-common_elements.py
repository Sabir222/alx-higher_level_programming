#!/usr/bin/python3
# def common_elements(set_1, set_2):
#     com_set = []
#     for i in set_2:
#         if i in set_1:
#             com_set.append(i)
#     return com_set


# def common_elements(set_1, set_2):
#     return [i for i in set_2 if i in set_1]


def common_elements(set_1, set_2):
    return set_1 & set_2
