def rightAngleTriangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a ** 2 + b ** 2 == c ** 2 or c ** 2 + b ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2: 
        return True
    else:
        return False

print(rightAngleTriangle(3, 4, 5))
print(rightAngleTriangle(-3, 4, 5))
print(rightAngleTriangle(3, 4, 50))


#9.

"""
Factorial = int(input("please give use a factorial? \n"))

while startNumber < Factorial:
    #print(startNumber, '\n')
    startNumber += 1
    multiply = startNumber *  multiply

print('Factorial: ', multiply)
"""

#2

def calculateFactorial(N):
    
    startNumber = 1
    multiply = 1
    
    while startNumber < N:
        startNumber += 1
        multiply = startNumber * multiply
    return multiply

print(calculateFactorial(5))
print(calculateFactorial(0))

#3

wordString1 = 'paper and the s in files count'
wordString2 = 'paper paper and the s in files count'
wordString3 = 'paper chase'
wordString4 =  'red paper files'
wordString5 = 'sss rrrrr abcdef'

def countWords(wordString):
    wordString = wordString.lower()
    x= wordString.split()
    count = 0
    for entry in x: 
        if entry[-1] == 'r' or entry[-1] == 's':
            count += 1
    return count


print('wordString 1: ', countWords(wordString1))
print('wordString 2: ', countWords(wordString2))
print('wordString 3: ', countWords(wordString3))
print('wordString 4: ', countWords(wordString4))
print('wordString 5: ', countWords(wordString5))

#4
aString = 'paper paper and the s in files count'


def findDuplicates(aString):
    uy = []
    for x in set(aString):
        #print(x)
        uz = []
        if aString.count(x) > 1: #compares that particular letter with the whole string
            #print('x:', str(x), ' and count: ', str(aString.count(x)))
            u = 'letter:'+ str(x) + ' count: '+ str(aString.count(x))
            uz.append(u)
            #print(u)
            #print(uz)
        uy.extend(uz)
    return uy
        
print(findDuplicates(aString))

#def duplicate_count(s):
#    return len([x for x in set(s) if s.count(x) > 1])


def duplicate_count(s):

    newList = []

    for x in set(s):
        if s.count(x) > 1:
            newList.append(x)

    return len(newList)



print(duplicate_count('bccbbbbbb'))
print(duplicate_count('abcdef'))
print(duplicate_count('HGF hdgf'))
print(duplicate_count('##12ab'))