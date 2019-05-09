#!/usr/bin/python2

```
This script takes an eDNA output file (with columns of different locations and taxonomy information in the last one), and will extract the species name (if applicable)

Usage = python2 scriptdraft.py inputfile geographicregion

```

import re
import string 
import sys
import os

inputfile = sys.argv[1]
create a file called unusable.txt 

with open(inputfile, "r") as my_file:
	for each column after the 1st one, not including the last one:
		make a temporary file called columnheader.txt
		go down each column and if it comes across a value != 0:
			if there is a white space after the last ;:
				<colummnname> : <entry in the last column of that line (the taxonomic data)?> >> unusable.txt
			if there is no white space after the last ;:
				split the line at the last ;
				grab the last item in the line (the species name)
				save the speies in the temporary file for that line


