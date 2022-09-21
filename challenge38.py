#Python > Collections > Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

#HackerRank
if __name__ == '__main__':
    N = int(input()); #Number of rows

    # Takes input, trim spaces, returns the resulting str as the namedtuple names for parameters.
    colNames = tuple([x.strip(' ') for x in input().split()])
    Student = namedtuple('Student', " ".join(colNames));
    
    StudentsT = [];
    for i in range(N):
        tmpInput = input().split()
        StudentsT.append(Student._make(tmpInput))
    
    averageMarks = sum([float(x.MARKS) for x in StudentsT]) / N;
    print(format(averageMarks, '.2f'))

#NOTAS:
#Otra aproximación: https://www.hackerrank.com/challenges/py-collections-namedtuple/forum/comments/793045

'''
  Hay tres formas para obtener un número con x cantidad de decimales:
  - "{%}".format(str)
  - format(str, '%')
  - f'{%}'
'''