#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    lArr = len(arr);
    pos = 0;
    zer = 0;
    neg = 0;
    
    for i in arr:
        if i > 0:
            pos += 1;
        elif i == 0:
            zer += 1;
        elif i < 0:
            neg += 1;
        else:
            print("SWW :(")
    
    print('{:6f}\n{:6f}\n{:6f}'.format(pos/lArr, neg/lArr, zer/lArr));

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

#OTRA APROXIMACIÓN: @reddyjahnavi
#En esta se hace uso de la list comprehension, luego de las f-string.
'''
n = int(input().strip())
arr = [1 if int(temp)>0 else -1 if int(temp)<0 else 0 for temp in input().strip().split(' ') ]
print("{0:.6f}".format(arr.count(1)/n))
print("{0:.6f}".format(arr.count(-1)/n))
print("{0:.6f}".format(arr.count(0)/n))
'''