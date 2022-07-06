def printSeconds(lista):
  scores = [];
  for a in lista:
    scores.append(a[1]);

  lowToHighScores = sorted(list(set(scores)));

  secondLowestStudents = [];
  for a in lista:
    if a[1] == lowToHighScores[1]:
      secondLowestStudents.append(a[0]);

  secondLowestStudents = sorted(secondLowestStudents)
  for s in secondLowestStudents:
    print(s);

#HackerRank
'''if __name__ == '__main__':
    students = [];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score]); #revisar
    printSeconds(students);'''

#Testing:
'''score = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]'''

#Notas:
'''
Se puede hacer uso de las "List comprehension" para hacer ciclos for de forma mas compacta.

Enlace para mas info: 
https://www.programiz.com/python-programming/list-comprehension
'''