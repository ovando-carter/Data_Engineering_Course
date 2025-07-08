from __future__ import print_function
import os.path
from pyspark.sql.functions import split
import sys
from operator import add
from pyspark.sql import SparkSession
from pyspark import SparkContext
sc =SparkContext()
 
filename = "/Users/apple/Documents/coding/companies/FDM/FDM_training/pyspark/data/olympics/cities.csv"
 
fileRDD = sc.textFile(filename)
#print(fileRDD.collect())
 
if filename.endswith(".txt"):
   splitit=" "
else:
   splitit=","
fileWordsRDD = fileRDD.flatMap(lambda line: line.split(splitit))
#for element in fileWordsRDD.collect():
#  print(element)
#print(fileWordsRDD.count())
 
def wordCount(wordListRDD):
    occurance=wordListRDD.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
    return occurance
 
newWord=fileWordsRDD
wordsCounter = wordCount(newWord)
#print(wordsCounter.collect())
 
wordAre = wordsCounter.sortBy(lambda x: -x[1])
#print(wordAre.collect())
print("Word\t\tNumber of Occurances")
for (element, counter) in wordAre.collect():
  print("%s\t\t\t%i" % (element, counter))
#print(wordAre.persist().is_cached)
wordAre.count()
print(wordAre.count())
#wordAre.saveAsTextFile("/FileStore/tables/foundwords.txt") 


print(wordAre.count())
print(wordAre.collect())


wordsDF = wordAre.toDF()
newDFIs=wordsDF.withColumnRenamed("_1", "Word").withColumnRenamed("_2", "Occurance")
newDFIs.show(wordsDF.count())


wordAre.toDebugString


filename = "/FileStore/tables/foundwords.txt/part-00000"
 
 
 
fileRDD = sc.textFile(filename)
print(fileRDD.collect())
