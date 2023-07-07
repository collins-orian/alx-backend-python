#!/usr/bin/env python3

'''task is to write a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies
a float by multiplier'''


def make_multiplier(multiplier: float):
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func