# dictionaries
print("use {} to declare dictionaries")
my_dict = {}
print(my_dict)
data_type = type(my_dict)
print(data_type, '\n')

print("the structure of dictionary is based on {key:value}")
my_dict = {'a': 0, 'b': 10, 'c': 100}
print(my_dict)
print("we can get the value by searching the key")
b_value = my_dict['b']
print(b_value, '\n')
# note that keys are always strings but values can be any data type such as float, integer, string, list, dictionary, etc.


print("we can add a key:value")
my_dict['d'] = 200
print(my_dict, '\n')

print("we can overwrite the value of a key")
my_dict['a'] = 5
print(my_dict, '\n')

print("use .keys() to get the keys")
keys = my_dict.keys()
print(keys)
keys = list(keys)
print(keys, '\n')

print("or use .value() to get the values")
values = my_dict.values()
print(values)
values = list(values)
print(values)
