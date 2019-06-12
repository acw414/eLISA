#!/bin/bash

# This is the main script for eLISA; it runs the Python code and then the R code
# It takes two inputs : the input file and the country that the samples were collected from
# Usage = sh eLISA.sh inputfile.txt "country name"

inputerror=".........
WARNING: INPUT ERROR.
eLISA requires two inputs - the name of your input file and the country the samples were collected from in quotation marks.
Example usage:
	sh eLISA.sh inputfile.txt "united states"
Please check inputs and try again
........."

. /u/local/Modules/default/init/modules.sh

if [ "$#" != "2" ]; then # If there are an incorrect number of inputs then an error message will be shown
        echo "$inputerror"
else
    	module load python/3.1
        echo "........."
        echo "Sorting input file"
        python ./Python_eLISA.py $1 # Runs Python_eLISA.py on the given input file
        echo "........."
        sed -i '/^$/d' finalsamplecolumn*.txt # Removes any blank lines from the temporary files outputted by Python_eLISA.py
        echo "Searching species database"
        echo "........."
        module load R/3.4.0
        Rscript ./R_eLISA.r $2 # Runs R_eLISA.r using the country name specified in the input
        echo "........."
        echo "Finalizing output"
	rm ./finalsamplecolumn*.txt # Deletes temporary files
        echo "........."
fi
