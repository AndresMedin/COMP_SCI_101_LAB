###           ###
### Grades.py ###
###           ###

import math

def median(values:list):
    length = len(values)
    values = sorted(values)
       
    if values == []:
        raise ValueError
    elif length % 2 == 0:
        med1 = int((length/2) - 1)
        med2 = int(length/2)
        median = float(values[med1] + values[med2])/2
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
