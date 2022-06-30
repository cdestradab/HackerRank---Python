#!/bin/python3

import math
import os
import random
import re
import sys

def isWeird(n):
    if (n % 2 != 0):
        return "Weird";
    elif (n in range(2,6)) and (n >= 19):
        return "Not Weird";
    else:
        return "Not Weird";

if __name__ == '__main__':
    n = int(input())
    print(isWeird(n));