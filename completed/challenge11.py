def promedion(iterable, qname):
    suma = 0;
    for i in iterable[qname]:
        suma += i

    return "{:.2f}".format((suma/len(iterable[qname])));


#MAIN:
'''if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    print(promedion(student_marks, query_name));'''

#Notas:

'''
Para cambiar la cantidad de decimales en el resultado aquí se hace uso del método "String format()", así:

float = 2.154327
format_float = "{:.2f}".format(float)

Mas métodos para definir la cantidad de decimales:
https://pythonguides.com/python-print-2-decimal-places/
'''