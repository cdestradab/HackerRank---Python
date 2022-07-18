#Python>Strings>Mutations
def mutate_string(string, position, character):
    newstr = string[:position] + character + string[position+1:];
    return newstr;

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#NOTA
'''
OPCION 1: Convertir la string en una lista, modificar y luego unir nuevamente en una string.

OPCION 2: Separar dos pedazos de la string, agregar el caracter a convenir y volver a unir.
'''