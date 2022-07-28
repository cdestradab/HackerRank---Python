# Python > Itertools > itertools.permutations()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations;

myLine, length = input().split();

myPermutation = ["".join(i) for i in ([*permutations(myLine, int(length))])]


print(*(sorted(myPermutation)), sep="\n");

#NOTAS:
'''
- Linea 5: Recordar que input no funciona si no se escribe en forma de función: input(). Y si no funciona no se pueden usar sus métodos.

- Linea 7: Los corchetes [] permiten definir una lista, y dentro de ellos se pueden usar expresiones de lista para construir listas sin necesidad de ciclos for extensos.

- Linea 7 y 10: Los paréntesis () permiten definir y encapsular una expresión. De manera que si la expresión dentro del paréntesis está bien definida se pueden usar los métodos que le corresponden al objeto resultante de dicha expresión.
'''