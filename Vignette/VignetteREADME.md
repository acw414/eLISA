# Vignette ReadMe

**Running eLISA with example datasets**   

This document will walk through a sample running of eLISA. 

Steps for running the program:  
1) The user should first install the [originr package](https://github.com/ropensci/originr) in R.
   - Log into the UCLA Hoffman2 server and type:
      ```
      module load R
      R
        > install.packages("originr")
       ```
   - The package may take up to 10 minutes to install, please do not close R or the terminal window. 
2) Then the user should then close R:
   ```
   quit()
   ```
3) They should move the input file into the eLISA directory (if necessary), navigate into the directory, and type the command:
   ```
   sh FinalBashCode.sh Fishsamplefile.txt
