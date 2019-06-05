#!/usr/bin/python2

#This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one), and will extract the species name (if applicable)

#Usage = python codedraft.py inputfile

# Imports the required functions to Hoffman

import re
import string
import sys
import os

delimitererror = ("""
WARNING: DELIMITER ERROR
eLISA requires taxonomic data seperated by semicolons.
For example:
        Eukaryota;Streptophyta;Bryopsida;Bryales;Bryaceae;Gemmabryum;Gemmabryum dichotomum
Please check input file and try again.
""")

inputfile = sys.argv[1]
openfile = open(inputfile, "r")

# Works out the number of samples (the number of columns) in the input file, and adds the header of each to a masterlist

with open(inputfile, "r") as f:
        h = f.readline()
        header = h.split("\t")
        headlen = len(header)
        colrange = range(1,headlen - 1)

masterlist = [0]

for x in colrange:
        masterlist.append(header[x])

# For each line with species data in the input file, if the column value is more than 0, the species name will be added to the end of the column header in the masterlist. 

openfile.readline() #skips the 1st line
for line in openfile:
        line = line.strip()
        Col = line.split("\t")
        if len(Col) == headlen:
                for x in colrange:
                        if Col[x] != "0":
                                if ';' not in line:
                                        print delimitererror
                                else:
                                     	sp = line.split(';')[-1]
                                        masterlist[x] =  masterlist[x] + ';' + sp
              
# Makes a file for each sample; writes the masterlist corresponding to that sample

for i in colrange:
        filename = "column" + str(i) + ".txt"
        with open(filename, 'w') as output:
                output.write(masterlist[i])
                  
# Puts each species on seperate lines; removes any repeats
# Deletes temporary files
# Creates files for each sample with the names finalsamplecolumnX.txt, with X being the column that sample was in

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
