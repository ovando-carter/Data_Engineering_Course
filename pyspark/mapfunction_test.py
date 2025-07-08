from __future__ import print_function
import os.path
from pyspark.sql.functions import split
import sys
from operator import add
from pyspark.sql import SparkSession
from pyspark import SparkContext


occurance=wordListRDD.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

# Map
arg1 = x
expression1 = (x, 1)
lam1_func = lambda(arg1:expression1)


# The map function takes in a function and an iterable(list, tuple, etc.) as an 
# input; applies passed function to each item of an iterable and returns a map 
# object(an iterator). i.e. iteratable = range(1, 10, 2), will iterate over every 
# odd number
map(function, iteratable)

# only needs an iteratable if you are trying to do a loop
# Takes a function and returns a map
map(lam1_func)


# Reduce 
arg2 = x,y
expression2 = x + y
lam2 = lambda(arg2:expression2)


# i think the reduce function takes in the map function as an 
# initializer but it does this by doing map.reduce()
reduce(function, iterable, [, initializer])

reduce(lam2_func)

map(lam1_func).reduce(lam2_func)