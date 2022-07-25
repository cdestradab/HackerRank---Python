#Python > String > Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    allLines = s.split('\n');
    newDoc = [];
    
    for line in allLines:
        words = line.split(' ');
        capWords = [];
        for word in words:
            capWord = word.capitalize();
            capWords.append(capWord);
        newDoc.append(" ".join(capWords));
    
    return ("\n".join(newDoc));
        
            
    print(s);
    return s;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#NOTA:
'''
Notar en el método split(), que si el parámetro se deja vacio, Python ignorará TODOS los espacios. Pero si se deja con el valor ' ' (un espacio) dividirá todos los caracteres solo por un espacio, eso significa que si hay tres caracteres de espacio, el caracter de en medio también será considerado un caracter como cualquier otro  no será ignorado.
'''
#OTRA APROXIMACIÓN:
'''
a_string = input().split(' ')
print(' '.join((word.capitalize() for word in a_string)))
'''