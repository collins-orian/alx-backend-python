#!/usr/bin/env python3

'''task is to write a type-annotated function sum_list which takes a list 
input_list of floats as argument and returns their sum as a float.'''


def sum_list(input_list: list[float]) -> float:
    '''the function takes in a parameters of list of float type
    and returns the sum of the parameters as a float'''

    return float(sum(input_list))
