#Python > Collections > DefaultDict Tutorial
#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict

def takeNInputsToList(n):
    newList = [];
    for _ in range(n):
        newList.append(input());
    return newList;

# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = map(int, input().split());
listA = takeNInputsToList(a);
listB = takeNInputsToList(b);

d = defaultdict(list);

for i in range(len(listA)):
    if listA[i] in listB:
        d[listA[i]].append(i+1);

for word in listB:
    if word not in d:
        d[word].append(-1);

for word in listB:
    print(*d[word]);

#NOTES:
'''
Esta aproximación no es muy eficiente en términos de entrega de reto, ya que hace uso de mas recursos con el propósito de que sea mas comprensible, y sus métodos se puedan usar en otros retos.

- defaultdict() es una subclase collección que hereda métodos de la clase dict() convencional. Tiene algunas aplicaciones interesantes como el conteo de valores.
Mas info: https://docs.python.org/3/library/stdtypes.html#dict-views

- Este código sería mas eficiente si en vez de hacer una lista se trabajara directamente con los inputs() y separando cada rango con los valores n y m. (Otra aproximación dif al final)
'''

#OTRA APROXIMACIÓN:
'''
from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,raw_input().split())

for i in range(0,n):
    d[raw_input()].append(i+1) 

for i in range(0,m):
    list1=list1+[raw_input()]  

for i in list1: 
    if i in d:
        print " ".join( map(str,d[i]) )
    else:
        print -1
'''