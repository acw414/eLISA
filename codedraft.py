#!/usr/bin/python2

#This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one), and will extract the species name (if applicable)

#Usage = python2 scriptdraft.py inputfile  

import re
import string 
import sys
import os

inputfile = sys.argv[1]

openfile = open(inputfile, "r")
for line in openfile:	
	Line = line.strip()
	#print Line	
	Col = line.split("\t")
	#print Col[0]
	if Col[1] != "0": #if the item in the 2nd column does not equal 0
		print "yaya" #this was just a placeholder to see if it worked. sorry
		#it should split the last item in the row at the last ; and then 
		#if there is a blank space after then that whole last chunk of taxonomy data gets added to a list called 'unusable, or sth. 
		#if there is no blank space then that species name should be added to the list whose name is the column header
	if Col[1] == "0":
		print "no" #osryr thiis was a placeholder too
		#if no then do nothing? maybe we dont even include a no statement?
#this should repeat for all columns except Col[0] (the 1st one) and Col[-1] (the last one w the species data
