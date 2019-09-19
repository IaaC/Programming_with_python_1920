# encoding: utf-8

##################################################
# This script interacts with data files to extract information and modify values given to a function.
# It is part of an exercise in which data about districts and neighbourhoods are processed
# Here we have the second part of the script that calls an external script to read neighbourhoods data
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

# Here we refer to the third-party scripts
import disctlib.district as d
import disctlib.neighbour as n


# Here some global variables to set paths and other details
districts_path = '../Data/districts_BCN.csv'
neighbourhoods_path = '../Data/neighbourhoods_BCN.csv'

n.read_neighbourhoods(neighbourhoods_path)

d.read_districts(districts_path)

# We need to define a method that aggregates information from neighbourhoods from the same district



