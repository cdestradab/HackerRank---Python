import textwrap

def wrap(string, max_width):
    wrappedString = '';
    for i in range(0,len(string),max_width):
        wrappedString = wrappedString + string[i:i+max_width] + '\n';
    return wrappedString;

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#NOTA:
'''
Una forma mas eficiente de realizar este reto es usando la librería textwrap y su método textwrap.wrap() o textwrap.fill()
'''