"""

 #######                               ####### 
    #    ######  ####  #####     ####  #       
    #    #      #        #      #    # #       
    #    #####   ####    #      #    # ######  
    #    #           #   #      #  # #       # 
    #    #      #    #   #      #   #  #     # 
    #    ######  ####    #       ### #  #####  
                                               
"""

from q5 import longestPalindrome as test_function

PROMPT1 = "Enter the string of letters"
RESULT = "The longest palindrome is"

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n"+PROMPT1+": ")
    if first == "q":
        break

    result = test_function(first)
    print("\t"+RESULT+": "+str(result))
