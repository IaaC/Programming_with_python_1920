# encoding: utf-8

##################################################
# This script shows an example of variable assignment.
# First, it shows different options for using arithmetic operators.
# This operators allow to perform basic arithmetic calculus.
#
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We don't need any library so far

# Let's write our code

print('These are few examples of arithmetic operators in python\n')

# We have already used addition: (+) and subtraction (-). Let's mix them with multiplication (*) and division (/)
result = 1 * 2 + 6 / 3
print('The result of calculating - 1*2 + 6/3 - is:')
print(result)
print('Do not forget the concept of precedence within arithmetic operators. '
      'There are differences when using operators in different positions')
result = 1 + 2 - 3 * 4 / 5
print('The result of - 1 + 2 - 3 * 4 / 5 -: ')
print(result)
result = 1 / 2 * 3 - 4 + 5
print('Is different than the result of - 1 / 2 * 3 - 4 + 5 -: ')
print(result)
