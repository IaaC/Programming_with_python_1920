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

# option 1:
numbers = all [0:11]
text = all [11:]
print (numbers)
print (text)

# option 2:
numbers = []
text = []
for i in all:
    if type(i) == int:
        numbers.append(i)
    else:
        text.append(i)
print (numbers)
print (text)

###############################################################################################################
# task2: we have shuffled the list "all".
# create again the three lists of even numbers, odd numbers and names (order of items is not important)

random.shuffle(all)

odd_numbers = []
even_numbers = []
text = []

for i in all:
    if type(i) == int:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    else:
        text.append(i)

print (odd_numbers)
print (even_numbers)
print (text)