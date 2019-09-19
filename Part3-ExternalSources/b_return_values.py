# encoding: utf-8

##################################################
# This script shows an example of a script using functions as a way to simplify programming.
# This functions can also return more than one value
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

def get_proportions(values, names, label):
    answer_template = '%s from %s is %f times %s from %s'
    proportions = []
    proportions.append(round(values[0] / values[1], 1))
    proportions.append(round(values[0] / values[2], 1))
    proportions.append(round(values[1] / values[2], 1))

    print(answer_template % (label, names[0], proportions[0], label, names[1]))
    print(answer_template % (label, names[0], proportions[1], label, names[2]))
    print(answer_template % (label, names[1], proportions[2], label, names[2]))



def get_averages(values1, values2):
    average1 = sum(values1) / len(values1)
    average2 = sum(values2) / len(values2)
    return average1, average2


##################################################
# and now we have the section for our source code
cities = {'names': ['Barcelona', 'Lisbon', 'Amsterdam'],
          'population': [5474482, 2827514, 2431000],
          'unemployment_rate': [17.24, 7.4, 3.3],
          'gdb_billions': [173, 72, 154]}
text_template = 'Average population is: %f \n Average unemployment rate is: %f'

val1, val2 = get_averages(cities['population'], cities['unemployment_rate'])

print(text_template % (val1, val2))

get_proportions(cities['gdb_billions'], cities['names'], 'GDP')
