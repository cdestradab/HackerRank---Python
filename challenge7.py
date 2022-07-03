#Set .intersection() Operation

def howManyForBoth(set1, set2):
    inters = set1.intersection(set2);
    return(len(inters));

if __name__ == '__main__':
    englishNews = int(input())
    englishNewsSet = set(input().split(' '))
    frenchNews = int(input())
    frenchNewsSet = set(input().split(' '))
    
    print(howManyForBoth(englishNewsSet,frenchNewsSet));

#The method split(sep='') does the trick for spliting values separated by some character.