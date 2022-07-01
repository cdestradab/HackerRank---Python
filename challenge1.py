#!/bin/python3

import math
import os
import random
import re
import sys

def isWeird(n):
    if (n == 0) or (n % 2 != 0):
        return "Weird";
    elif (n in range(2,6)) or (n >= 21):
        return "Not Weird";
    elif (n in range(6,21)):
        return "Weird";
    else:
        return "Not Weird";

def test1():
  for n in [0,4,8,6,20,21,22]:
    print(n, "returns ", ch1.isWeird(n));

'''
if __name__ == '__main__':
    n = int(input())
    print(isWeird(n));
'''