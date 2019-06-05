#!/bin/bash

#This is the main script for eLISA
#It runs the Python code and then the R code
#It takes the file to be analyzed as the input
#Usage = sh eLISA.sh inputfile.txt

inputerror=".........
WARNING: INPUT ERROR.
eLISA requires one input - the name of your input file.
Example usage:
	sh eLISA.sh inputfile.txt
Please check input and try again
........."

. /u/local/Modules/default/init/modules.sh

if [ "$#" != "1" ]; then
        echo "$inputerror"
else
    	module load python/3.1
        echo "........."
        echo "Sorting input file"
        python ./Scripts/Python_eLISA.py $1
        echo "........."
        sed -i '/^$/d' finalsamplecolumn*.txt
        echo "Searching species database"
        echo "........."
        module load R/3.4.0
        Rscript ./Scripts/R_eLISA.r
        echo "........."
        echo "Finalizing output"
	rm ./finalsamplecolumn*.txt
        echo "........."
fi
