#Python > Itertools > itertools.product()

from itertools import product;

def takeAllInputs():
    inputs = [];
    
    try:
        while True:
            inp = input();
            if inp == "":
                break;
            else:
                inputs.append(inp);
    except EOFError:
        pass;
    return tuple(inputs);

def convertInputsToTuples(l):
    newList = [tuple(map(int, i.split(" "))) for i in l];
    return newList;
    


myInputs = takeAllInputs();
myMatrices = convertInputsToTuples(myInputs);

print(*product(*myMatrices));

#NOTAS:
'''
- Sobre takeAllInputs(): Se comprende la importancia de saber lidiar con los errores de ejecución y como crear excepciones adecuadas.

- Sobre convertIinputsToTuples(l): Recordar que para hacer uso de las "list expressions", la expresión SIEMPRE debe estar dentro de corchetes para que tenga efecto.

- product() es un método del módulo itertools que permite hallar el producto matricial de dos o más raices, incluso se puede usar una sola matriz y ejecutar el método repitiendo la misma matriz.
Mas info: https://docs.python.org/2/library/itertools.html#itertools.product

- *list: Al poner un asterisco antes de un objeto lista lo que ocurre es que se "despliega" todo su contenido, muy usado en list expressions y en conjunción con el método map().

- map(): Es un método que permite obtener un objeto iterable no definido, se pueden editar sus elementos ajustando los parámetros. En este caso en la función convertInputsToTuples() se aprovechan las características de map() para convertir los elementos de una lista que son strings, y se pasan a int.

- Al desplegar una lista (*Lista) dentro de un print() lo que sucede es que se despliega la lista y se imprimen en pantalla uno a uno los valores de la lista separados por un espacio.
'''
#UNA APROXIMACIÓN MAS DIRECTA:
'''
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))
'''