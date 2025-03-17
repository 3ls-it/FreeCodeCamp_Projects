#!/data/data/com.termux/files/usr/bin/env python3
import numpy as np
from math import sqrt



def calculate(list: list) -> dict:

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    a1_mu, a1_var, a1_sigma, a1_max, a1_min, a1_sum = 0, 0, 0, 0, 0, 0
    a2_mu, a2_var, a2_sigma, a2_max, a2_min, a2_sum = 0, 0, 0, 0, 0, 0
    flat_mu, flat_var, flat_sigma, flat_max, flat_min, flat_sum = 0, 0, 0, 0, 0, 0

    ## Helper functions 
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


    flat_mu = _mean(list)
    flat_var = _variance(list)
    flat_sigma = _sigma(list)
    flat_max = max(list)
    flat_min = min(list)
    flat_sum = sum(list)


    ## Define return dict 
    """
    {
      'mean': [axis1, axis2, flattened],
      'variance': [axis1, axis2, flattened],
      'standard deviation': [axis1, axis2, flattened],
      'max': [axis1, axis2, flattened],
      'min': [axis1, axis2, flattened],
      'sum': [axis1, axis2, flattened]
    }
    """
    calculations = {
                    'mean': [a1_mu, a2_mu, flat_mu],
                    'variance': [a1_var, a2_var, flat_var],
                    'standard deviation': [a1_sigma, a2_sigma, flat_sigma],
                    'max': [a1_max, a2_max, flat_max],
                    'min': [a1_min, a2_min, flat_min],
                    'sum': [a1_sum, a2_sum, flat_sum]
                   }


    ## Test prints 
    """
    print()
    print(list)
    print('Arithmetic mean:', flat_mu)
    print('Variance:', flat_var)
    print('Std deviation:',flat_sigma)
    print('Max:', flat_max)
    print('Min:', flat_min)
    print('Sum:', flat_sum)
    print()
    """

    return calculations
# End calculate() 


nums = [0,1,2,3,4,5,6,7,8] 
nums2 = [1]
nums3 = [0,1,2,3,4,5,6,7,8,9]
stats = calculate(nums)
print(stats)
print()
#calculate(nums2)
#calculate(nums3)
