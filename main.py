def isTheHighest(arr,pos):
    print(arr)
    print(pos)
    unsortedList = arr;
    print(unsortedList)
    sortedList = unsortedList.sort(reverse=True);
    print(sortedList)
    return sortedList[pos]

n = int("5")
arr = list(map(int, "2 3 6 6 5".split()))
print(isTheHighest(arr, 1))