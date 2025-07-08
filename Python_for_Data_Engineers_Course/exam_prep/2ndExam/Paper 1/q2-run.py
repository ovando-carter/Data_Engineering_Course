"""

 #######                                #####  
    #    ######  ####  #####     ####  #     # 
    #    #      #        #      #    #       # 
    #    #####   ####    #      #    #  #####  
    #    #           #   #      #  # # #       
    #    #      #    #   #      #   #  #       
    #    ######  ####    #       ### # ####### 

"""

from q2 import numberOfOccurrencesInString as test_function

PROMPT1 = "Enter the string"
RESULT = "The number of occurrences"

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n"+PROMPT1+": ")
    if first == "q":
        break

    result = test_function(first)
    print("\t"+RESULT+": "+str(result))
