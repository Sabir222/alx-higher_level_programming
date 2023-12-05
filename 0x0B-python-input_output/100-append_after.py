#!/usr/bin/python3
'''
fer
'''


def append_after(filename="", search_string="", new_string=""):
    '''ing'''
    with open(filename, "r+") as file:
        lines = file.readlines()
        changed = []
        for line in range(len(lines)):
            changed.append(lines[line])
            if search_string in lines[line]:
                changed.append(new_string)

        file.seek(0)
        file.write("".join(changed))
