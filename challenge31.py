#Python > Math > Polar Coordinates

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

z = complex(input());

print(abs(z));
print(cmath.phase(z));



#NOTA:
'''
La función complex() permite convertir un string en un número complejo siempre que tenga la forma x+bj;

Mas info sobre cmath y como convertir numeros complejos a coodernadas polares:
https://docs.python.org/3.8/library/cmath.html
'''