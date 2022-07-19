def checksCharacters(cha):
    hasAlpha = False;
    hasDigit = False;
    hasAlphaNum = False;
    hasLower = False;
    hasUpper = False;
    
    for j in cha:
        if (not hasAlpha):
            hasAlpha = j.isalpha();
        if (not hasDigit):
            hasDigit = j.isdigit();
        if (not hasLower):
            hasLower = j.islower();
        if (not hasUpper):
            hasUpper = j.isupper();
    
    hasAlphaNum = hasAlpha or hasDigit;
            
    print(hasAlphaNum, hasAlpha, hasDigit, hasLower, hasUpper, sep='\n')
    return 0;
        
if __name__ == '__main__':
    s = input()
    checksCharacters(s);

#NOTA:
'''
Hay que tener cuidado con el flujo que se le da a los condicionales. Especialmente con el "if" y un "elif" anidado. En este caso por ejemplo, no se puede usar elif, porque el propósito es evaluar todas las posibilidades en un mismo caracter. Pero si se usa un elif, y la condición del if principal no se cumple nunca, el elif en el no será tenido en cuenta siquiera. Raro. Hay que investigar más.
'''