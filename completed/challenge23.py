#Python > String > String Formatting

def print_formatted(number):
    width = len(bin(number)[2:]);
    table = ""
    
    for i in range(1, number + 1):
        deci = str(i);
        octa = oct(i)[2:];
        hexa = hex(i)[2:].upper();
        bina = bin(i)[2:];
        
        table = table + deci.rjust(width) + " " + octa.rjust(width) + " " + hexa.rjust(width) + " " + bina.rjust(width) + "\n";
    
    print(table);
    return(table);

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#NOTAS:
'''
Conceptos necesarios para realizar este reto:
- Conocer los métodos predefinidos bin(), hex(), oct().
- Conocer el método str.rjust().

Considerar:
- Siempre verificar y hacer una lista de los prerequisitos solicitados para no estar perdiendo el tiempo.
'''

#Solución alternativa usando new format
'''
n = int(raw_input())
width = len("{0:b}".format(n))
for i in xrange(1,n+1):
  print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)

#REFERENCIA: https://pyformat.info/
'''