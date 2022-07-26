#Python>Strings>Find a string

def count_substring(string, sub_string):
    n = 0;
    for i in range(0, len(string)):
        if (sub_string == string[i:i+len(sub_string)]):
            n += 1;
    return n;

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#NOTA:
'''
String es una función de la clase string, que permite remover los espacios a los lados, si se añade un caracter o string como parametro, buscará este valor y lo removerá por ambos lados, dejando solo lo que haya entre ellos.
'''

#NOTA:
'''
Otras aproximaciones:
- Usar el método .startswith("")
'''