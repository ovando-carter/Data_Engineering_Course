"""

 #######                                #####  
    #    ######  ####  #####     ####  #     # 
    #    #      #        #      #    #       # 
    #    #####   ####    #      #    #  #####  
    #    #           #   #      #  # #       # 
    #    #      #    #   #      #   #  #     # 
    #    ######  ####    #       ### #  #####  

"""

from q3 import percentageUnderTenPounds as test_function

PROMPT1 = "Enter prices separated by commas or spaces"
RESULT = "The percentage under 10 Pounds"

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n"+PROMPT1+": ")
    if first == "q":
        break

    if first == "":
        continue

    while ' ' in first:
        first = first.replace(' ', ',')
    while ',,' in first:
        first = first.replace(',,', ',')
    first = first.strip(',')

    prices = []
    for price in first.split(','):
        prices.append(float(price))

    result = test_function(prices)
    print("\t"+RESULT+": "+str(result))
