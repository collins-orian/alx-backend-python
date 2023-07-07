#!/usr/bin/env python3

'''task is to write a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies
a float by multiplier'''

from types import callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    '''Creates a multiplier function'''
    return lambda param: param * multiplier
