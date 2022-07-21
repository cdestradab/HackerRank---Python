# Python > Strings > Designer Door Mat
def genMat(n,m,pattern, background, message):
    newMat = ""
    midPattern = int(((n-1)/2))
    
    for i in range(0, midPattern):
        newMat = newMat + (pattern*((i*2)+1)).center(m, background) + '\n';
    
    newMat = newMat + message.center(m, background) + '\n';
    
    for i in range(midPattern, 0, -1):
        newMat = newMat + (pattern*((i*2)-1)).center(m, background) + '\n';
    
    return newMat;


if __name__ == '__main__':
    n, m = input().split();
    print(genMat(int(n),int(m),'.|.','-', 'WELCOME'))

#NOTA:
'''
En este caso el método str.center(width, 'char') funcionó de maravilla. Queda la función allí para usos posteriores (quizás).
'''