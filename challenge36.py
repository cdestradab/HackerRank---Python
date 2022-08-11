#Python > Errors and Exceptions > Incorrect Regex
#https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
tCases = int(input());

for _ in range(tCases):
    s = input();
    isRegex = True;
    
    try:
        _a = re.match(s, "example123");
    except re.error:
        isRegex = False;
    
    print(isRegex);

#NOTAS:
'''
- Aqui lo primero que se me ocurrió fué usar las expresiones regulares con el módulo "re". Cualquier error me informaría que dicha expresión regular no tiene la sintaxis correcta. Asi que en la excepción pongo una bandera que me avisa que dicha RegEx es FALSA.

- El módulo "re" tiene un método llamado .compile, que verifica una expresión regular y devuelve un objeto "re".
Si se usa bool() en ese objeto, y es correcto, devolverá TRUE.
'''
#OTRA APROXIMACIÓN:
'''
import re

def isvalidregex(regex):
    try: re.compile(regex)
    except re.error: return False
    return True

for i in range(int(input())):
    print(isvalidregex(input()))
'''

#OTRA APROXIMACIÓN:
'''
import re
for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print('False')
'''