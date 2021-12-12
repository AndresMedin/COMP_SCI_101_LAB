###           ###
### Grades.py ###
###           ###

import math

def median(values:list):
    values = sorted(values)
    length = len(values)
    if values == []:
        raise ValueError
    elif length % 2 == 0:
        mid1 = int((length/2) - 1)
        mid2 = int(length/2)
        median = float(values[mid1] + values[mid2])/2
        return median
    else:
        median = values[int((length-1)/2)]
        return median

def average(values:list):
    if values == []:
        return math.nan
    else:
        sum_values = sum(values)
        avg = sum_values/len(values)
        return float(avg)       

def total(values:list):
    return sum(values)
