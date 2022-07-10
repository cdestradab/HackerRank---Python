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

#Note:
'''Nota: Hay una alternativa para poder evaluar directamente entradas de texto en forma de comandos. Los metodos eval() y getattr().

El método eval() es mas riesgoso, ya que usado con un comando input podria permitir a un usuario explotar las vulnerabilidades del código.

El método getattr() es una mejor opción en cuanto a seguridad, porque siendo similar a eval(), restringe su uso a una clase y evalua la entrada para buscar ya sea el método o variable en la clase.'''