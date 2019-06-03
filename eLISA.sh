#!/bin/bash

#This will be the main script for the program
#It will run the Python script and then the R script
#It will just take the file to be analyzed as the input
#Usage = sh bashscript inputfile.txt

inputerror=".........
WARNING: INPUT ERROR.
/namebofourprogram/ requires one input - the name of your input file.
Example usage:
	sh eLISA.py inputfile.txt
Please check input and try again
........."

. /u/local/Modules/default/init/modules.sh

if [ "$#" != "1" ]; then
        echo "$inputerror"
else
    	module load python/3.1
        echo "........."
        echo "sorting input file"
        python eLISA_python_code.py $1
        echo "........."
        sed -i '/^$/d' finalsamplecolumn*.txt
        echo "searching species database"
        module load R/3.4.0
        R CMD BATCH eLISA_R_code.r
        echo "........."
        echo "finalizing output table"
	rm ./finalsamplecolumn*.txt
        echo "........."
fi
