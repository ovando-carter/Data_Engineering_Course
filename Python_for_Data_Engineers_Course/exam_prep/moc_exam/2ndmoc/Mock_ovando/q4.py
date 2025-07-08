def findDuplicates(s):

    newList = []

    for x in set(s):
        if s.count(x) > 1:
            newList.append(x)

    return len(newList)