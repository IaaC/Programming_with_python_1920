# tuples
print("tuples are very similar to lists")
print("the are defined by ()")
my_tuple = (1, 2, 3)
print(my_tuple)
data_type = type(my_tuple)
print(data_type, '\n')

print("tuples can have different data types as items")
my_tuple = ('One', 'Two', 3)
print(my_tuple, '\n')

print("you can use indexing and slicing for tuples")
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[0:2], '\n')

# print ("the difference between tuples and lists is that tuples are 'immutable'. This means once they are assigned they cannot be reassigned.")
# my_list = [1,2,3,4]
# my_tuple = (1,2,3,4)
# my_list[0] = 'ONE'
# print (my_list)
# my_tuple[0] = 'ONE'
# print (my_tuple)
# # tuples are useful when you want to make sure your elements will not change during the program
