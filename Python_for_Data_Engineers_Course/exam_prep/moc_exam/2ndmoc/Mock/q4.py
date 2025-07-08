def findDuplicates(s):

    newList = []

    for x in set(s):
        if s.count(x) > 1:
            newList.append(x)

    return len(newList)

'''
# dictionary method
def findDuplicates(inpString):

    charCount = {}
    count = 0

    #For each char in the string
    for char in inpString:
        charCount[char] = inpString.count(char)

    for x in charCount.values():
        if x > 1:
            count = count + 1

    return count
'''

'''
# instructor version
def findDuplicates(input_string):
    chars = list(input_string)
    chars.sort()
    current = ' '
    duplicates = []
    counter = 0
    for i in range(len(chars)): 
        if chars[i] != current and input_string.count(chars[i]) > 1:
            duplicates.append(chars[i])
            current = chars[i]
    return len(duplicates)
