def countWords(wordString):
    #make sure they are all lower case and then split the letters up into a list
    x= wordString.lower().split()

    count = 0

    for entry in x: 
        if entry[-1] == 'r' or entry[-1] == 's':
            # increase the count everytime it finds either and r or an s
            count += 1
    return count