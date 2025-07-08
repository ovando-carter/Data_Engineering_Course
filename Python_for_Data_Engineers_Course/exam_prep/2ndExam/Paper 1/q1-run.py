"""

 #######                                 #   
    #    ######  ####  #####     ####   ##   
    #    #      #        #      #    # # #   
    #    #####   ####    #      #    #   #   
    #    #           #   #      #  # #   #   
    #    #      #    #   #      #   #    #   
    #    ######  ####    #       ### # ##### 

"""

from q1 import minimumWage as test_function

PROMPT1 = "Enter the person's age"
RESULT = "Their minimum wage is"

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n"+PROMPT1+": ")
    if first == "q":
        break

    result = test_function(int(first))
    print("\t"+RESULT+": "+str(result))
