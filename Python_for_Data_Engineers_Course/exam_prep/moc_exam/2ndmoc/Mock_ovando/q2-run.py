"""

 #######                                #####  
    #    ######  ####  #####     ####  #     # 
    #    #      #        #      #    #       # 
    #    #####   ####    #      #    #  #####  
    #    #           #   #      #  # # #       
    #    #      #    #   #      #   #  #       
    #    ######  ####    #       ### # ####### 

"""

from q2 import calculateFactorial as test_function

PROMPT1 = "Enter an integer"
RESULT = "The factorial is"

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n"+PROMPT1+": ")
    if first == "q":
        break

    if int(first) >= 45:
        print("\t"+RESULT+": TRY AGAIN - Test with numbers less than 45")
        continue
        
    result = test_function(int(first))
    print("\t"+RESULT+": "+str(result))
