"""
    Task	: 01_2
    Author	: Phumipat C. [MAGCARI]
    Language: Python
    Created	: 04 December 2021 [12:40]
    Algo	: 
    Status	: 
"""
import numpy as np

with open('01.in', 'r') as f:
    num = [int(x) for x in f.read().split()]

num = np.array(num)
sum = num[:-2] + num[1:-1] + num[2:]
dif = np.diff(sum)
sign = np.sign(dif)

print(np.sum(sign == 1))
