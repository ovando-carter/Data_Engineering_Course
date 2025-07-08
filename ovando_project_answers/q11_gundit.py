def solution(word, char, posi):
    
    new_list = [] # new list
    
    # From Q1
    def ordinary_higher(string):
        function1 = lambda string : string[:posi] + char + string[posi+1:]
        return function1(string)
    
    # set up for loop to go through every element in list of strings
    for string in word:
        
        # add elements of string list to new list after undergoing lambda function
        new_list = [ordinary_higher(string) for string in word]
    
    return new_list