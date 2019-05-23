#!/usr/bin/python2

#This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one), and will extract the species name (if applicable)

#Usage = python2 codedraft.py inputfile

import re
import string
import sys
import os

inputfile = sys.argv[1]
openfile = open(inputfile, "r")
sample1 = []
sample2 = []
output1 = open("sample1.txt", "w")
output2 = open("sample2.txt", "w")
for line in openfile:
        Line = line.strip()
        Col = line.split("\t")
        if Col[1] != "0" and len(Col) >3: #if the item in the 2nd column does not equal 0 and the number of columns is > 3
                Elementlist = line.split(';')[-1] #split the line at the last ;
                sample1.append(Elementlist) #append this to the list sample1 (in line 13)
                output1.write(Elementlist) #write elementlist to the temp file outputCG. idk how this is different ot the line above or why u write Elementlist and not sample1?? idk confusing
        if Col[2] != "0" and len(Col) >3:
                Element_list = line.split(';')[-1]
                sample2.append(Element_list)
                output2.write(Element_list)

#need to work out how to do this for all columns in a doc, each creating a new file called sample1 sample2 etc.
#and yeah mauybe we dont need to do the count for Thurs, i can do that after
output1.close()
output2.close()
#need to find a way to remove instances of duplication in output file
#need to assign the specific sample name to the output file row1, not the entire 1st line from input file
