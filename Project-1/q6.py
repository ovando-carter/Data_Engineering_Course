# returns a list of strings obtained from the input list
# the input list of strings of equal length
# every string the character at the specified position is replaced with the given character
# The ordinary function solution() must consist of one return statement alone,
# • the map() built-in function OR
# • list comprehension OR
# • generator comprehension


def solution(word , char, posi):
    # use map like a for loop
    return list(map(lambda x: x[:posi] + char + x[posi +1:],word))






