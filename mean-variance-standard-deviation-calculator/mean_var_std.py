#!/usr/bin/env python3
import numpy as np


def calculate(list: list) -> dict:

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)
    trans = matrix.transpose()

    a1_mu = [float(np.mean(trans[0])), float(np.mean(trans[1])), float(np.mean(trans[2]))]
    a1_var = [float(np.var(trans[0])), float(np.var(trans[1])), float(np.var(trans[2]))]
    a1_sigma = [float(np.std(trans[0])), float(np.std(trans[1])), float(np.std(trans[2]))]
    a1_max = [int(np.max(trans[0])), int(np.max(trans[1])), int(np.max(trans[2]))]
    a1_min = [int(np.min(trans[0])), int(np.min(trans[1])), int(np.min(trans[2]))]
    a1_sum = [int(np.sum(trans[0])), int(np.sum(trans[1])), int(np.sum(trans[2]))]

    a2_mu = [float(np.mean(matrix[0])), float(np.mean(matrix[1])), float(np.mean(matrix[2]))]
    a2_var = [float(np.var(matrix[0])), float(np.var(matrix[1])), float(np.var(matrix[2]))]
    a2_sigma = [float(np.std(matrix[0])), float(np.std(matrix[1])), float(np.std(matrix[2]))]
    a2_max = [int(np.max(matrix[0])), int(np.max(matrix[1])), int(np.max(matrix[2]))]
    a2_min = [int(np.min(matrix[0])), int(np.min(matrix[1])), int(np.min(matrix[2]))]
    a2_sum = [int(np.sum(matrix[0])), int(np.sum(matrix[1])), int(np.sum(matrix[2]))]

    flat_mu = float(np.mean(list))
    flat_var = float(np.var(list))
    flat_sigma = float(np.std(list))
    flat_max = int(np.max(list))
    flat_min = int(np.min(list))
    flat_sum = int(np.sum(list))


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


    return calculations
# End calculate() 

