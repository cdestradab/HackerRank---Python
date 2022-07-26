#Python > Strings > The Minion Game

def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    
    slen = len(string);
    sStuart = 0;
    sKevin = 0;
    
    ite = 0;
    while ite < 1: #slen:
        for i in range(slen-ite):
            if string[i] in vowels:
                sKevin += slen - i;
            else:
                sStuart += slen - i;
        ite += 1;

    if sKevin > sStuart:
        print("Kevin", sKevin);
    elif sStuart > sKevin:
        print("Stuart", sStuart);
    else:
        print("Draw");
        
    return 0;
    

if __name__ == '__main__':
    s = input()
    minion_game(s)

#NOTA:
'''
Para este desafío hay que notar que considerando los requerimientos del problema, para obtener el resultado no hace falta asegurarse de sentidos gramaticales ni comparaciones con el valor de entrada. Tampoco verificar si el substring realmente se repite, ya que por la forma como se puntúa se obtiene el mismo puntaje ya sea que se repitan x substings tanto si son identicos o diferentes.

Para este algoritmo se evalua el string de entrada UNA SOLA VEZ, y para cada caracter se evalua si es vocal o consonante, para luego añadir el puntaje correspondiente al "jugador" que le corresponde la vocal o la consonante, CONSIDERANDO las posibles veces que se podría repetir esa misma evaluación en próximas iteraciones.
'''