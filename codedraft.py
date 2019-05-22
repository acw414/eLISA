#!/usr/bin/python2

#draft script due in Thurs discussion. Will take fish taxonomy input file and output species from each sample in a list

#This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one), and will extract the species name (if applicable)

#Usage = python2 scriptdraft.py inputfile  

#this just imports some functions
import re
import string 
import sys
import os

#this assgns the variable inputfile to the inputfile
inputfile = sys.argv[1]

openfile = open(inputfile, "r")
for line in openfile:	
	Line = line.strip()
	#print Line	
	Col = line.split("\t") #ok up to this point this has made a list of tuples called Col. everything above here is ok i think.
	#U can do "print Col" to check out how Col is organized.
	#Col a list containing other lists - each column is split into a list.
	#and you can call them too. like 'print Col[0]' will print everything in the 1st column. 
	#OH YEAH EVERYTIME U USE 'COL' ITS GOT TO BE (AT LEAST) AT THIS LEVEL OF INDENT bc the variable only exists within this for loop. 
	if Col[1] != "0": #if the item in the 2nd column does not equal 0. Daniel said we dont have to do lots of for loops and can go straight into an if statement. 
		#but we want it to go through all the lists in Col, not just Col[1], so ya we need to work that out.
		print "yaya" #this was just a placeholder to see if it worked. sorry
		#it should split the last item in the row at the last ; and then 
		#if there is a blank space after then that whole last chunk of taxonomy data gets added to a list called 'unusable, or sth. 
		#if there is no blank space then that species name should be added to the list whose name is the column header
	if Col[1] == "0":
		print "no" #osryr thiis was a placeholder too
		#if no then do nothing? maybe we dont even include a no statement?
	
#this should repeat for all columns except Col[0] (the 1st one) and Col[-1] (the last one w the species data)
