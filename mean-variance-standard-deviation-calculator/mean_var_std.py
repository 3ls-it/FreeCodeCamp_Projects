#!/data/data/com.termux/files/usr/bin/env python3
import numpy as np
from math import sqrt



def calculate(list: list) -> dict:

    def _mean(n_list: list) -> float:
        if not n_list:
            raise ValueError('List can not be empty.')
        return sum(n_list) / len(n_list)
    # End _mean() 

    def _variance(n_list: list) -> float:
        if not n_list:
            raise ValueError('List can not be empty.')
        mu = _mean(n_list)
        return sum((x - mu) ** 2 for x in n_list) / len(n_list)
    # End _variance() 

    def _sigma(n_list: list) -> float:
        if not n_list:
            raise ValueError('List cannot be empty')
        var = _variance(n_list)
        return sqrt(var)
    # End _sigma() 


    print()
    print(list)
    print('Arithmetic mean:', _mean(list))
    print('Variance:', _variance(list))
    print('Std deviation:', _sigma(list))
    print('Max:', max(list))
    print('Min:', min(list))
    print('Sum:', sum(list))
    print()

    #return calculations
# End calculate() 


nums = [0,1,2,3,4,5,6,7,8] 
calculate(nums)
