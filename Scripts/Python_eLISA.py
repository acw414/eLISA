#!/usr/bin/python2

# This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one) and will extract the names of any species present
# It will output a file called finalsamplecolumn.txt per column, which will list all the species found in that sample with no repeats
# Python_eLISA.py can be run by itself to produce these output files, but to analyse whether the species are invasive the user should run this through eLISA.sh

#Independent usage = python Python_eLISA.py inputfile.txt

#Intended usage = sh eLISA.sh inputfile.txt "country name"

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

# Defines the input file as the 1st argument given after the script name

inputfile = sys.argv[1]
openfile = open(inputfile, "r")

# Works out the number of samples in the file (the number of columns excluding the first and last ones)

with open(inputfile, "r") as f:
        h = f.readline()
        header = h.split("\t")
        headlen = len(header) 
        colrange = range(1,headlen - 1) 

masterlist = [0]

# Adds the header of each sample column to the masterlist 

for x in colrange:
        masterlist.append(header[x])

# For each line with species data in the input file, if the column value is more than 0, the species name will be added to the end of the corresponding column header in the masterlist. 

openfile.readline() #skips the 1st line
for line in openfile:
        line = line.strip()
        Col = line.split("\t")
        if len(Col) == headlen:
                for x in colrange:
                        if Col[x] != "0":
                                if ';' not in line: #if taxonomic data in the last column is not seperated by semicolons, this will print an error message
                                        print delimitererror
                                else:
                                     	sp = line.split(';')[-1]
                                        masterlist[x] =  masterlist[x] + ';' + sp # Appends ';species name' to the end of the corresponding column header in the masterlist. 
              
# Makes a file for each sample; writes the masterlist corresponding to that sample

for i in colrange:
        filename = "column" + str(i) + ".txt"
        with open(filename, 'w') as output:
                output.write(masterlist[i])
               
# Defines the current working directory

path = os.listdir('.')

for filename in path:
        if 'column' in filename:
                outfile1 = str('sample') + filename
                with open(filename, "r") as inn:
                        sep =  inn.read().replace(';','\n') # Replaces each semicolon in the masterlist with a new line
                with open(outfile1, "w+") as out:
                        out.write(sep)
                unique = []
                outfile2 = "final" + outfile1
                openoutfile2 = open(outfile2, "w")
                for line in open(outfile1,"r"):
                        if line not in unique: # Removes any repeated species
                                openoutfile2.write(line)
                                unique.append(line)
                os.remove(outfile1) # Deletes temporary files
                os.remove(filename)
