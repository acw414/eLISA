#!/usr/bin/python2

#This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one), and will extract the species name (if applicable)

#Usage = python2 codedraft.py inputfile

import re
import string
import sys
import os

inputfile = sys.argv[1]
openfile = open(inputfile, "r")

#This works out the number of columns in the input file

with open(inputfile, "r") as f:
        h = f.readline()
        header = h.split("\t")
        headlen = len(header)
        colrange = range(1,headlen - 1)

masterlist = [0]

for x in colrange:
        masterlist.append(header[x])

openfile.readline() #skips the 1st line
for line in openfile:
        line = line.strip()
        Col = line.split("\t")
        if len(Col) == headlen:
                for x in colrange:
                        if Col[x] != "0":
                                sp = line.split(';')[-1]
                                masterlist[x] =  masterlist[x] + ';' + sp
for i in colrange:
        filename = "column" + str(i) + ".txt"
        with open(filename, 'w') as output:
                output.write(masterlist[i])

# Puts each species on seperate lines; removes any repeats

path = os.listdir('.')

for filename in path:
        if 'column' in filename:
                outfile1 = str('sample') + filename
                with open(filename, "r") as inn:
                        sep =  inn.read().replace(';','\n')
                with open(outfile1, "w+") as out:
                        out.write(sep)
                unique = []
                outfile2 = "final" + outfile1
                openoutfile2 = open(outfile2, "w")
                for line in open(outfile1,"r"):
                        if line not in unique:
                                openoutfile2.write(line)
                                unique.append(line)
                os.remove(outfile1)
                os.remove(filename)

path = os.listdir('.')

# now need to work out how to rename the output file as the sample name

for filename in path:
        if 'finalsamplecolumn' in filename:
                openfile = open(filename, "r")
                with openfile as f:
                        for line in f:
                                if char.isdigit() in line:
                                        print line
#                       firstline = f.readline()
#                       print firstline
