#Python > Strings > Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here.
    # k is the length of a chunk
    n = len(string); #Length of string
    nsubs = int(n/k); #Number of chunks
    lChunks = [];
    
    
    for i in range(0, n, k):
        chunk = "";
        
        for j in string[i: i+k]:
            if j not in chunk:
                chunk = chunk + j;
        lChunks.append(chunk);

    print(*lChunks, sep = "\n")
    return lChunks;

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#NOTA:
'''
Recordar siempre leer todos los elementos del problema propuesto: valores de entrada, restricciones y respuesta esperada.

Ver la linea 18, es una herramienta muy buena para imprimir valores de una lista sin usar ciclos for.
'''

#OTRA APROXIMACIÓN MUY SOFISTICADA:
'''
S, N = input(), int(input()) 
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
'''
# En esta se hace uso conjunto de las funcionalidades del método zip y las características de los iteradores (iter()). Un iterador, a diferencia de otros iterables, mantiene internamente un punto de progreso sobre el cual se va avanzando en los elementos. Por eso en este problema los elementos no se repiten en la linea 35
#Mas info: https://www.hackerrank.com/challenges/merge-the-tools/forum