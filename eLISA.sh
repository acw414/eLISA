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
        echo "sorting input file"
        python python_eLISA.py $1
        echo "........."
        sed -i '/^$/d' finalsamplecolumn*.txt
        echo "searching species database"
        module load R/3.4.0
        Rscript R_eLISA.r
        echo "........."
        echo "finalizing output table"
	rm ./finalsamplecolumn*.txt
        echo "........."
fi
