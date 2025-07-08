"""

 #######                                 #   
    #    ######  ####  #####     ####   ##   
    #    #      #        #      #    # # #   
    #    #####   ####    #      #    #   #   
    #    #           #   #      #  # #   #   
    #    #      #    #   #      #   #    #   
    #    ######  ####    #       ### # ##### 

"""

from q1 import rightAngledTriangle as test_function

PROMPT1 = "Enter length of side 1"
PROMPT2 = "Enter length of side 2"
PROMPT3 = "Enter length of side 3"
RESULT = "Right angled triangle"

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n"+PROMPT1+": ")
    if first == "q":
        break

    second = input(PROMPT2+": ")
    if second == "q":
        break

    third = input(PROMPT3+": ")
    if third == "q":
        break

    result = test_function(int(first), int(second), int(third))
    print("\t"+RESULT+": "+str(result))
