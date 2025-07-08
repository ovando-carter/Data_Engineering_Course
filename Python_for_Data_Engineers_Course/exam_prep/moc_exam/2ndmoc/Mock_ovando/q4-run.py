"""

 #######                               #       
    #    ######  ####  #####     ####  #    #  
    #    #      #        #      #    # #    #  
    #    #####   ####    #      #    # #    #  
    #    #           #   #      #  # # ####### 
    #    #      #    #   #      #   #       #  
    #    ######  ####    #       ### #      #  

"""

from q4 import findDuplicates as test_function

PROMPT1 = "Enter a string"
RESULT = "Count of duplicates is"

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n"+PROMPT1+": ")
    if first == "q":
        break

    result = test_function(first)
    print("\t"+RESULT+": "+str(result))
