englishNews = '9'
englishNewsSet = set("1 2 3 4 5 6 7 8 9".split(sep=' '))
frenchNews = '9'
frenchNewsSet = set("10 1 2 3 11 21 55 6 8".split(sep=' '))

def howManyForBoth(set1, set2):
  print(set1)
  print(set2)
  
  inters = set1.intersection(set2);
  return(len(inters));
  
print(howManyForBoth(englishNewsSet,frenchNewsSet));