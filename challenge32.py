#Python > Sets > Introduction to Sets
#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):
    # your code goes here
    h = set(array);
    return ( "{:.3f}".format(sum(h)/len(h)) );

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#NOTES:
'''
- Un set() es una colección de elementos, desordenada y sin elementos repetidos. Se usa principalmente para verificar si un valor está en determinada colección.

- Aquí se usó los f-strings para configurar la cantidad de decimales que salen en pantalla.
MAS INFO: https://pyformat.info/#simple

- Desde Python 3.6 los f-strings se pueden escribir de dos formas:
f"{x:}"
"{}".format(x)

x es una variable.
'''