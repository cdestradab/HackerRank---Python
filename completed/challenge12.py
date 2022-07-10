def listCommand(lista, comando, listaEntradas=0):
    if comando == 'insert':
        lista.insert(listaEntradas[0], listaEntradas[1]);
    elif comando == 'print':
        print(lista);
    elif comando == 'remove':
        lista.remove(listaEntradas[0]);
    elif comando == 'append':
        lista.append(listaEntradas[0]);
    elif comando == 'sort':
        lista.sort();
    elif comando == 'pop':
        lista.pop();
    elif comando == 'reverse':
        lista.reverse();
    else:
        print('Algo pasa!!!');

#HackerRank Main
'''if __name__ == '__main__':
    N = int(input())
    lista = [];
    for i in range(N):
        comando, *entradas = input().split();
        listaEntradas = list(map(int, entradas));

        listCommand(lista, comando, listaEntradas);'''

#Manual Testing
'''
listaEjemplo = [];
listCommand(listaEjemplo, 'insert', [0,85]);
listCommand(listaEjemplo, 'insert', [3,45]);
listCommand(listaEjemplo, 'insert', [1,57]);
listCommand(listaEjemplo, 'print');
listCommand(listaEjemplo, 'remove', [45]);
listCommand(listaEjemplo, 'append', [20]);
listCommand(listaEjemplo, 'sort');
listCommand(listaEjemplo, 'print');
listCommand(listaEjemplo, 'pop');
listCommand(listaEjemplo, 'print');
listCommand(listaEjemplo, 'reverse');

print(listaEjemplo);
'''