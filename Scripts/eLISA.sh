#!/bin/bash

#This is the main script for eLISA
#It runs the Python code and then the R code
#It takes the file to be analyzed as the input
#Usage = sh eLISA.sh inputfile.txt "country"

inputerror=".........
WARNING: INPUT ERROR.
eLISA requires two inputs - the name of your input file and the country the samples were collected from in quotation marks.
Example usage:
	sh eLISA.sh inputfile.txt "united states"
Please check inputs and try again
........."

. /u/local/Modules/default/init/modules.sh

if [ "$#" != "2" ]; then
        echo "$inputerror"
else
    	module load python/3.1
        echo "........."
        echo "Sorting input file"
        python ./Python_eLISA.py $1
        echo "........."
        sed -i '/^$/d' finalsamplecolumn*.txt
        echo "Searching species database"
        echo "........."
        module load R/3.4.0
        Rscript ./R_eLISA.r $2
        echo "........."
        echo "Finalizing output"
	rm ./finalsamplecolumn*.txt
        echo "........."
fi
