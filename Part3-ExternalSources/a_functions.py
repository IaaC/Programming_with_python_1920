# encoding: utf-8

##################################################
# This script shows an example of a script using functions as a way to simplify programming.
# This is a common structure
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

# We don't need libraries for this script


##################################################
# We have a temporal section for defining functions
def say_hi(given_name):
    print('Hi', given_name)


def a_function(argument_1, argument_2):
    print('I received this arguments')
    print('Argument 1: ' + str(argument_1))
    print('Argument 2: ' + str(argument_2))
    # Functions are used to manage operations

    # sometimes they return values
    answer = 'a_function was executed'
    return answer


##################################################
# and now we have the section for our source code
name = 'type your name here'
say_hi(name)

var1 = 'abc'
var2 = 123

a_function(var1, var2)
