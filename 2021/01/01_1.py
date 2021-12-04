"""
    Task	: 01_1
    Author	: Phumipat C. [MAGCARI]
    Language: Python
    Created	: 04 December 2021 [12:29]
    Algo	: 
    Status	: 
"""
import numpy as np

with open('01.in', 'r') as f:
    num = [int(x) for x in f.read().split()]

num = np.array(num, dtype=int)
dif = np.diff(num)
sign = np.sign(dif)

print(np.sum(sign == 1))
