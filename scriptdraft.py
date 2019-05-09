#!/usr/bin/python2

```
This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one), and will extract the species name (if applicable)

Usage = python2 scriptdraft.py inputfile 

```

import re
import string 
import sys
import os

inputfile = sys.argv[1]

open(unusable.txt,"w+")

with open(inputfile, "r") as my_file:
	for all columns after the first (not including the last one):
		counter_columnnumber = 0
		make a temporary file called columnheader.txt
		go down each column and if it comes across a value != 0:
			if there is a white space after the last ;:
				<colummnname> : <taxonomic data> >> unusable.txt
			if there is no white space after the last ;:
				counter_columnnumber = counter_columnnumber + 1
				split the line at the last ;
				grab the last item in the line (the species name) in columnheader.txt

