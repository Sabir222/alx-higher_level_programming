#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        return None, None
    elif len(sentence) == 0:
        return 0, None
    else:
        return len(sentence), sentence[0]
