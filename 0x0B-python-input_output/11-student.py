#!/usr/bin/python3
'''
fnt
'''


class Student:
    ''' ass '''

    def __init__(self, first_name, last_name, age):
        ''' Cod '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' ter '''
        res = {}
        if attrs:
            for attr in attrs:
                if attr in self.__dict__:
                    res[attr] = self.__dict__[attr]
        else:
            for attr in self.__dict__:
                res[attr] = self.__dict__[attr]

        return res

    def reload_from_json(self, json):
        ''' ance '''
        for attr in json:
            self.__dict__[attr] = json[attr]
