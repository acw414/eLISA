#!/usr/bin/python2

#This script takes the Fish_taxonomy_file.txt, and will output a text file per sample location containing all the species sampled there (with no repeats)

#Usage = python2 codedraft.py Fish_taxonomy_file.txt

import re
import string
import sys
import os

inputfile = sys.argv[1]
openfile = open(inputfile, "r")
sample1 = []
sample2 = []
output1 = open("s1temp.txt", "w")
output2 = open("s2temp.txt", "w")
for line in openfile:
        Line = line.strip()
        Col = line.split("\t")
        if Col[1] != "0" and len(Col) >3: #if the item in the 2nd column does not equal 0 and the number of columns is > 3
                Elementlist = line.split(';')[-1] #split the line at the last ;
                sample1.append(Elementlist)
                output1.write(Elementlist)
        if Col[2] != "0" and len(Col) >3:
                Element_list = line.split(';')[-1]
                sample2.append(Element_list)
                output2.write(Element_list)

output1.close()
output2.close()

unique1 = set() # holds unique species in sample 1
outfile1 = open("sample1.txt", "w")
for line in open("s1temp.txt", "r"):
        if line not in unique1: #if the species is not a duplicate
                outfile1.write(line)
                unique1.add(line)
                
outfile1.close()
os.remove("s1temp.txt")

unique2 = set() # holds unique species in sample 2
outfile2 = open("sample2.txt", "w")
for line in open("s2temp.txt", "r"):
        if line not in unique2: #if the species is not a duplicate
                outfile2.write(line)
                unique2.add(line)
outfile2.close()
os.remove("s2temp.txt")
