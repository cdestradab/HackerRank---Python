#Not a method, it is used to set a py document as the main.
'''
if __name__ == '__main__':
  #Code goes here.
'''


# This method is useful when there are going to be n different inputs. It returns a list with n elements with the values of those inputs.
def takeNInputsToList(n):
    newList = [];
    for _ in range(n):
        newList.append(input());
    return newList;