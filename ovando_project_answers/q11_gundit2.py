'''
# The higher order function can be defined as an ordinary or lambda function 
def solution(strings, char, posi, func):
    
    new_list = []

    for word in strings:
        # passed lambda function for q1 as an argument to the higher 
        # order function, or returned from a higher order function
        new_list.append(str(func(word, char, posi)))

    return new_list

  
strings = ['$153.25', '$100.50', '$199.99', '$300.00']
char = '£'
posi = 0


replace_ch_in_pos = solution(strings, char, posi, lambda word, char, posi: word[:posi] + char + word[posi +1:])

#print(replace_ch_in_pos)
'''


word = ['$153.25', '$100.50', '$199.99', '$300.00']
char = '£'
posi = 0

def solution(word, char, posi):
    
    # From Q1
    def ordinary_higher(string):
        function1 = lambda string : string[:posi] + char + string[posi+1:]
        return function1(string)
    
       
    # add elements of string list to new list after undergoing lambda function
    new_list = [ordinary_higher(string) for string in word]
    
    return new_list

print(solution(word, char, posi))
