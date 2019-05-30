#!/bin/bash

#This will be the main script for the program
#It will run the Python script and then the R script
#It will just take the file to be analyzed as the input
#Usage = sh bashscript inputfile.txt

. /u/local/Modules/default/init/modules.sh

module load python/3

echo "........."
echo "sorting input file"
echo "........."

python codedraft1.py $1

sed -i '/^$/d' finalsamplecolumn*.txt

echo "searching spceies database"
echo "........."
