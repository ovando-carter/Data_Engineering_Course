"""

 #######                               #       
    #    ######  ####  #####     ####  #    #  
    #    #      #        #      #    # #    #  
    #    #####   ####    #      #    # #    #  
    #    #           #   #      #  # # ####### 
    #    #      #    #   #      #   #       #  
    #    ######  ####    #       ### #      #  

"""

from q4 import fillCrosswordLine as test_function

PROMPT1 = "Enter crossword string"
PROMPT2 = "Enter the word to fit "
RESULT = "The word fits as follows"

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n"+PROMPT1+": ")
    if first == "q":
        break

    second = input(PROMPT2+": ")
    if second == "q":
        break

    result = test_function(first, second)
    print("\t"+RESULT+": "+str(result))
