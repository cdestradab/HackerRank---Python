#Python > Strings > Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
    abt = " abcdefghijklmnopqrstuvwxyz";
    piramid = [];
    width = (size*2)-1;
    
    base = abt[1:size+1];
    for i in range(size,0,-1):
        line = "-".join(list(abt[i:size+1])).ljust(width,"-");
        line = (line[:0:-1] + line);
        piramid.append(line);
    
    print("\n".join(piramid + piramid[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#NOTA:
'''
Me ha tomado algo de tiempo, pero se pudo. Lo importante aquí es evitar concatenar strings independientes para que en los casos mas tangenciales también se apliquen correctamente los cambios.
'''

#SOLUCION ESTILIZADA:
'''
import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))
'''