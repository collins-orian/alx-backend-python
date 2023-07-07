#!/usr/bin/env python3

'''task is to write a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.'''

from typing import List, Union


def sum_mixed_list(mxd_lst:  List[Union[int, float]]) -> float:
    '''the function takes in a parameters of list of float type
    and returns the sum of the parameters as a float'''

    return float(sum(mxd_lst))
