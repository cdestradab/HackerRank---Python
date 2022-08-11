#Python > Errors and Exceptions > Exceptions
#https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
tCases = int(input());
for _ in range(tCases): 
    try:
        a, b = map(int, input().split(" "));
        print(a//b);
    except ZeroDivisionError as e:
        print("Error Code:", e);
    except ValueError as f:
        print("Error Code:", f);

#NOTAS:
'''
- Las excepciones son errores de ejecución, mas no de sintaxis. Un error de ejecución se puede "manejar" gracias al uso del método "try".
Mas info: https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions
'''