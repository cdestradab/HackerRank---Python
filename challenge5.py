#HackerRank
def is_leap(year):
    leap = False
    
    if (year%4==0):
      leap = True;
      if (year%100==0):
        leap = False;
        if (year%400==0):
          leap = True;
    
    return leap

year = int(input())
print(is_leap(year))

#Testing

'''import challenge5 as ch5;
years = [2000,2400,1800, 1900, 2100, 2200, 2300,2500,1990];

for i in years:
  print(ch5.is_leap(i));'''