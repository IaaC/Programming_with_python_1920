import random

###############################################################################################################
# inputs are three lists of even numbers, odd numbers and a list of names
# as well as a list with combination of all of the three lists together called "all"

even_numbers = [0,2,4,6,8,10]
odd_numbers = [1,3,5,7,9]
names = ["Leonard", "Trista", "Anneliese", "Susie", "Rocio", "Concetta", "Nancy", "Shea", "Ezra", "Maia"]

all = even_numbers + odd_numbers + names
print ("ordered list:\n",all)

###############################################################################################################
# task1: separate the "all" list into two lists of numbers and text



###############################################################################################################
# task2: we have shuffled the list "all".
# create again the three lists of even numbers, odd numbers and names (order of items is not important)

random.shuffle(all)
print ("shuffled list:\n", all)
