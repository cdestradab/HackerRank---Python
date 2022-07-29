#Python > Collection > collections.Counter

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = input(); # Number of shoes
stock = input().split(" "); # All shoe sizes in stock
avShoes = Counter(stock); #Available shoes (Dic key="size", value="shoes available")
cust = int(input()); #Number of customers
sale = 0;

for _ in range(cust):
    size, price = input().split();
    
    if int(avShoes[size]) > 0:
        avShoes[size] -= 1;
        sale += int(price);

print(sale);

#NOTAS:
'''
- El valor de Custom() funciona como un diccionario común y corriente, con sus métodos.
Mas info: 
https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
https://docs.python.org/2/library/collections.html#collections.Counter
'''