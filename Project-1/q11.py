# The higher order function can be defined as an ordinary or lambda function 
def solution(strings, char, posi):

    def ordinary_higher(strings, char, posi, func):
        # passed lambda function for q1 as an argument to the higher 
        # order function, or returned from a higher order function
        new_list = [str(func(word, char, posi)) for word in strings]

        return new_list
    
    replace_ch_in_pos = ordinary_higher(strings, char, posi, lambda word, char, posi: word[:posi] + char + word[posi +1:])

    return replace_ch_in_pos


