'''
# first attempt
def calculateFactorial(N):
    startNumber = 1 
    multiply = 1
    while startNumber < N: 
        startNumber += 1
        multiply = startNumber * multiply
    return multiply
'''

def calculateFactorial(N):
    mult = 1
    if N == 0:
        return 1
    elif N < 0:
        return 0
    else:
        for i in range(1,N):
            mult = mult * (i+1)
        return mult