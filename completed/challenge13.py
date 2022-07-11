if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)));

#NOTA:
'''El método hash() brinda una gran utilidad ya que Python crea un identificador para cada objeto inmutable como las tuplas y otros, a su vez este identificador es creado basado en el contenido del objeto. Esto significa que es posible comparar dos objetos con su identificador y así saber si efectivamente son iguales o no, sin tener que recurrir al uso de ciclos.'''