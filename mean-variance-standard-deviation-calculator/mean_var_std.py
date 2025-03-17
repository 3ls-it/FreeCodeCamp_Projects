#!/data/data/com.termux/files/usr/bin/env python3
import numpy as np



def calculate(list: list) -> dict:

    def _mean(n_list: list) -> float:
        return sum(n_list) / len(n_list)
    # End _mean() 

    def _variance(n_list: list) -> float:
        if len(n_list) == 0:
            raise ValueError("List can not be empty.")
        mu = _mean(n_list)
        return sum((x - mu) ** 2 for x in n_list) / len(n_list)
    # End _variance() 






    return calculations
# End calculate() 
