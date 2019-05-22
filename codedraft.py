#!/usr/bin/python2

#This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one), and will extract the species name (if applicable)

#Usage = python2 scriptdraft.py inputfile  

import re
import string 
import sys
import os

inputfile = sys.argv[1]
sample1 = []
openfile = open(inputfile, "r")
outputCG=open("sample1.txt", "w")
for line in openfile:   
        Line = line.strip()     
        Col = line.split("\t")
        if Col[1] != "0" and len(Col) >3: #if the item in the 2nd column does not equal 0
                Elementlist = line.split(';')[-1]       
                #sample1 = u/home/class/c177/c177-28/Project/sample1.txt                
                #f = open(sample1,"w+")
                sample1.append(Elementlist)
        #       Elementlist >> sample1.txt  #prints the last thing in the line (the species)
                outputCG.write(Elementlist)

                #       print "noo"
#               else:           
#                       print 'cannae'
#print "yaya" #this was just a placeholder to see if it worked. sorry 
                #if there is a blank space after then that whole last chunk of taxonomy data gets added to a list called 'unusable, or sth. 
#       if Col[1] == "0":
#               print "no" #osryr thiis was a placeholder too
                #if no then do nothing? maybe we dont even include a no statement?
#this should repeat for all columns except Col[0] (the 1st one) and Col[-1] (the last one w the species data

outputCG.close()
