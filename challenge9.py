def isTheHighest(arr,pos):
    sortedList = sorted(arr, reverse=True);
    return sortedList[pos];
    

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    print(isTheHighest(arr, 1))

'''Observacion # 1:
En la variable 'arr' hay que considerar lo siguiente:
- map convierte el valor del input en un objeto iterable
- set hace una colección con el objeto iterable, descartando los números repetidos.
- list convierte la colección en una lista

arr entonces es una lista, y una lista se puede organizar con la función sorted().'''

'''Observación # 2:
Hay una diferencia importante entre el método list.sort() y la función sorted():
- list.sort() permite organizar los elementos de la lista, pero no crea una lista nueva, solo devuelve los elementos ya organizados, pero estos permanecen en su sitio.
- sorted() si toma el objeto y devuelve una lista nueva organizada segun los criterios establecidos'''